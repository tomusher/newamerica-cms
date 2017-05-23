import { Component } from 'react';
import { connect } from 'react-redux';
import { NAME } from '../constants';
import ContentListItem from './ContentListItem';

class ContentList extends Component {
  render(){
    let { results } = this.props;
    return (
      <section className='content-list container'>
        {results.map((r, i)=>(
          <ContentListItem post={r} key={`content-list-item-${i}`}/>
        ))}
      </section>
    );
  }
}

const mapStateToProps = (state) => ({
  results: state[NAME].results || []
});

export default connect(mapStateToProps)(ContentList);
