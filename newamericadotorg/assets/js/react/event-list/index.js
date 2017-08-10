import { Component } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { NAME, ID } from './constants';
import { FutureEvents, PastEvents } from  './components/EventList';

class Events extends Component {
  componentWillMount(){
    this.state = { showPast: false };
  }
  showPast = () => {
    this.setState({ showPast: true });
  }
  render(){
    let { params } = this.props;
    return(
      <section className="container--medium event-lists">
        <FutureEvents params={params} />
        {!this.state.showPast &&
          <div className="event-lists__show-past-button-wrapper">
            <a className="button transparent lg event-lists__show-past-button" onClick={this.showPast}>
              Show Past Events
            </a>
          </div>
        }{this.state.showPast &&
          <PastEvents params={params} />
        }
      </section>
    );
  }
}

const APP = ({}) => (
  <Router>
    <Switch>
      <Route path="/events" component={Events} />
      <Route path="/:programSlug/events" render={({match: { params }})=>(
        <Events params={params} />
      )}/>
      <Route path="/:programSlug/:projectSlug/events" render={({match: { params }})=>(
        <Events params={params} />
      )}/>
    </Switch>
  </Router>
);

export default { NAME, ID, APP };
