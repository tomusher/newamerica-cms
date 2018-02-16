import { Component, cloneElement } from 'react';
import { connect } from 'react-redux';
import { PublicationListItem, Person } from './ContentCards';

export const LoadingDots = ({ color='black' }) => (
  <label className={`button--text loading-dots centered ${color} block`}>
    <span>.</span><span>.</span><span>.</span>
  </label>
);

export class PublicationsList extends Component {
  loadMore = () => {
    let { fetchAndAppend, setQueryParam, response } = this.props;
    if(!response.hasNext || response.isFetching) return;
    this.isLoadingMore = true;
    setQueryParam('page', response.page+1);
    fetchAndAppend(this.triggerScrollEvents);
  }

  triggerScrollEvents = () => {
    setTimeout(()=>{
      this.isLoadingMore = false;
      this.props.dispatch({
        type: 'TRIGGER_SCROLL_EVENTS',
        component: 'site'
      });
    });
  }

  render(){
    let { response, fetchAndAppend } = this.props;
    let { results, isFetching, hasNext } = response;
    if(results.length===0 && !isFetching){
      return (
        <label className="bold block centered">No results found</label>
      );
    }

    if(isFetching && !this.isLoadingMore){
      return (
        <div className="program__publications-list-wrapper">
          <div className="program__publications-list margin-top-60">
              <LoadingDots />
          </div>
        </div>
      );
    }

    return (
      <div className="program__publications-list-wrapper">
        <div className="program__publications-list">
            {results.map((post, i ) => {
              if(post.content_type.api_name == 'person')
                return ( <Person key={`post-${i}`} person={post} /> );
              return ( <PublicationListItem key={`post-${i}`} post={post} /> );
            })}
        </div>
        {hasNext &&
        <div className="program__publications-list-load-more margin-top-10">
          <label className={`button ${isFetching ? 'is-fetching' : ''}`} onClick={this.loadMore}>
            <span className="load-more-label">Load More</span>
            {isFetching && <span className="loading-dots--absolute">
              <span>.</span><span>.</span><span>.</span>
            </span>}
          </label>
        </div>}
      </div>
    );
  }
}

export class PublicationsWrapper extends Component {
  state = {
    filtersOpen: false
  }


  toggleMobileFilters = () => {
    this.setState({ filtersOpen: !this.state.filtersOpen });
  }
  render(){
    let { filters, publications } = this.props;
    return (
      <div className="program__publications row gutter-45 margin-top-lg-35">
        <div className={`program__publications__open-mobile-filter col-12 margin-top-35`}>
          <a className={`button--text with-caret--${this.state.filtersOpen ? 'up' : 'down'}`} onClick={this.toggleMobileFilters}>Filters</a>
        </div>
        <div className={`col-lg-3 margin-top-5 margin-bottom-15 program__publications__filter-col${this.state.filtersOpen ? ' open' : ''}`}>
          {filters}
        </div>
        <div className='col-12 col-lg-9 program__publications__list-col'>
          {publications}
        </div>
      </div>
    );
  }
}
