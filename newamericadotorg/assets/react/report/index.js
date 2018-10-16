import React, { Component } from 'react';
import { NAME, ID } from './constants';
import { Fetch, Response } from '../components/API';
import { Route, Switch, Redirect } from 'react-router-dom';
import { format as formatDate } from 'date-fns';
import GARouter from '../ga-router';
import DocumentMeta from 'react-document-meta';
import Heading from './components/Heading';
import Body from './components/Body';
import TopNav from './components/TopNav';
import BottomNav from './components/BottomNav';
import store from '../store';
import { setResponse } from '../api/actions';
import ContentMenu from './components/ContentMenu';
import OverlayMenu from './components/OverlayMenu';
import Attachments from './components/Attachments';
import FeaturedSections from './components/FeaturedSections';
import Authors from './components/Authors';

class Report extends Component {
  constructor(props){
    super(props);
    this.state = {
      menuOpen: false, contentsPosition: '0%', attchsOpen: false, showNextBtn: false,
      section: this.getSection(),
      attchClicked: false
    }
  }

  openMenu = (e) => {
    this.setState({ menuOpen: true });
  }

  closeMenu = (e) => {
    this.setState({ menuOpen: false });
  }

  showAttachments = () => {
    this.setState({ attchsOpen: true, attchClicked: true });
  }

  hideAttachments = () => {
    this.setState({ attchsOpen: false });
  }

  animateMenu = (position) => {
    this.setState({ contentsPosition: position });
  }

  getSection = () => {
    let { report, match: { params } } = this.props;

    if(!params.sectionSlug) return false;
    return report.sections.find((s)=>( s.slug==params.sectionSlug ));
  }

  anchorTag = () => {
    const anchor = this.props.location.hash.replace('#', '');

    if (anchor) {
      const el = document.getElementById(anchor);
      if (el) {
        const { top } = el.getBoundingClientRect();
        let positionY = top-140;
        window.scrollTo(0, positionY);
      }
      return true;
    }
  }

  componentDidMount(){
    let { report } = this.props;

    newamericadotorg.actions.addScrollEvent({
      selector: '.report',
      onTick: (el, dir, prog) => {
        //let pos = prog < 130/el.offsetHeight ? '0%' : (prog > (el.offsetHeight-500)/el.offsetHeight ? '0%' : '-100%');
        let { section } = this.state;

        let showNextBtn = report.sections.length !== section.number && prog > (el.offsetHeight-window.innerHeight)/el.offsetHeight ? true : false;

        this.setState({ showNextBtn });
      }
    });

    this.props.dispatch({
      type: 'RELOAD_SCROLL_EVENTS',
      component: 'site'
    });
    this.anchorTag();
    // react-router shim for oti colors
    if(this.props.report.programs.length > 0){
      if(this.props.report.programs[0].slug == 'oti') document.body.classList.add('oti');
    }
  }

  componentDidUpdate(prevProps, prevState) {

    if (this.props.location !== prevProps.location) {
      this.props.dispatch({
        type: 'RELOAD_SCROLL_EVENTS',
        component: 'site'
      });

      window.scrollTo(0, 0);
      this.setState({ section: this.getSection() });
    }

    if(this.state.section != prevState.section){
      this.anchorTag();
    }

  }

  render(){
    let { location, match, report, redirect } = this.props;
    let { showNextBtn, section, attchClicked } = this.state;

    let showHeading = !section || report.sections.length===1;
    let showAuthors = report.sections.length===1
    let showMenu = !section && report.sections.length > 1;
    let showBody = section || (!section && report.sections.length===1);
    let showOverlay = !!section;
    return (
      <DocumentMeta title={`${report.title}: ${section.title}`} description={report.search_description}>
        <div className={`report${report.sections.length===1 ? ' single-page' : ''}`}>
          <TopNav section={section} report={report}
            openMenu={this.openMenu}
            closeMenu={this.closeMenu}
            showAttachments={this.showAttachments}
            hideAttachments={this.hideAttachments}
            attchClicked={attchClicked}
            menuOpen={this.state.menuOpen} />
            {showHeading &&
              <Heading report={report}/>
            }

            {(showMenu && report.abstract) &&
              <div className="container margin-80" id="abstract">
                <h3 className="margin-top-0 margin-bottom-25">Abstract</h3>
                <div className="report__abstract" dangerouslySetInnerHTML={{ __html: report.abstract }}  style={{ maxWidth: '800px' }}/>
              </div>
            }

            {(showMenu && report.featured_sections.length > 0) &&
              <div className="container margin-80" id="featured">
                <h3 className="margin-top-0 margin-bottom-25">Featured Sections</h3>
                <FeaturedSections featuredSections={report.featured_sections} />
              </div>
            }

            {showMenu &&
              <div className="container margin-80" id="contents">
                <h3 className="margin-top-0 margin-bottom-25">Contents</h3>
                <ContentMenu report={report} closeMenu={this.closeMenu}/>
              </div>
            }

            {showMenu &&
              <div className="container margin-80" id="authors">
                <h3 className="margin-top-0 margin-bottom-25">Authors</h3>
                <Authors authors={report.authors} />
              </div>
            }

            {showBody && <Body section={section || report.sections[0]}
              report={report}
              dispatch={this.props.dispatch}
              location={location}
              closeMenu={this.closeMenu}/>
            }

            {showAuthors && <div className="container report__body single-page-body margin-0" id="authors">
              <div className="post-body-wrapper">
                <h3 className="margin-bottom-25">Authors</h3>
                <Authors authors={report.authors} md={true} />
              </div>
            </div>}

            {(showAuthors && report.acknowledgments) &&
              <div className="container report__body single-page-body margin-0" id="acknowledgments">
                <div className="post-body-wrapper">
                  <h3 className="margin-top-0 margin-bottom-25">Acknowledgments</h3>
                  <div className="report__acknowledgments" dangerouslySetInnerHTML={{ __html: report.acknowledgments }} />
                </div>
              </div>
            }

            {(showMenu && report.acknowledgments) &&
              <div className="container margin-80" id="acknowledgments">
                <h3 className="margin-top-0 margin-bottom-25">Acknowledgments</h3>
                <div className="report__acknowledgments" dangerouslySetInnerHTML={{ __html: report.acknowledgments }}  style={{ maxWidth: '800px' }}/>
              </div>
            }

          {showOverlay &&
            <OverlayMenu report={report}
                open={this.state.menuOpen}
                openMenu={this.openMenu}
                closeMenu={this.closeMenu}
                hideAttachments={this.hideAttachments}
                contentsPosition={this.state.contentsPosition}>
              <ContentMenu report={report} activeSection={section.slug} closeMenu={this.closeMenu} showHome={true}/>
            </OverlayMenu>
            }
          {showOverlay &&
            <BottomNav section={section}
              showNextBtn={showNextBtn}
              report={report}
              openMenu={this.openMenu}
              hideAttachments={this.hideAttachments}/>
          }
          {report.attachments.length > 0 &&
            <Attachments attachments={report.attachments}
              hideAttachments={this.hideAttachments}
              attchsOpen={this.state.attchsOpen}/>
          }
        </div>
      </DocumentMeta>
    );
  }
}

class Routes extends Component {
  reportRender = (props) => {
    let { response: { results }} = this.props;
    return (<Report {...props} dispatch={this.props.dispatch} report={results} />);
  }

  redirect = (props) => {
    let { response: { results }} = this.props;
    return <Redirect to={`${props.match.url}${results.sections[0].slug}`} />
  }

  render(){
    let { response: { results }} = this.props;
    if(!results) return null;
    return (
      <GARouter>
        <Switch>
          <Route path={`/admin/pages`} render={() => (
            <Redirect to={results.url} />
          )} />
          <Route path='/:program/reports/:reportTitle/:sectionSlug?' render={this.reportRender} />
          <Route path='/:program/:subprogram/reports/:reportTitle/:sectionSlug?' render={this.reportRender} />
        </Switch>
      </GARouter>
    );
  }
}

class APP extends Component {
  componentDidMount(){
      if(window.initialState){
        store.dispatch(setResponse(NAME, {
          count: 0,
          page: 1,
          hasNext: false,
          hasPrevious: false,
          results: window.initialState
        }));
      }
  }

  render(){
    let { reportId } = this.props;

    if(window.initialState) return <Response name={NAME} component={Routes} />

    return (
      <Fetch name={NAME}
      endpoint={`report/${reportId}`}
      fetchOnMount={true}
      component={Routes} />
    );
  }
}


export default { APP, NAME, ID };
