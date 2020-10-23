import './Search.scss';

import React, { useState, useEffect } from 'react';
import * as QueryString from 'query-string';

import { PublicationListItem, Person } from '../../components/ContentCards';
import { LoadingDots } from '../../components/Icons';


function groupBy(list, keyGetter) {
  const map = new Map();
  list.forEach((item) => {
    const key = keyGetter(item);
    const collection = map.get(key);
    if (!collection) {
      map.set(key, [item]);
    } else {
      collection.push(item);
    }
  });
  return map;
}

function classifyResult(result) {
  let type = result.content_type.api_name;

  if (type == "article" || type == "blogpost" || type == "book" || type == "event" || type == "issueortopic" || type == "podcast" || type == "policypaper" || type == "pressrelase" || type == "quoted" || type == "weeklyarticle" || type == "report" || type == "indepth") {
    return "Publications";
  } else if (type == "program" || type == "initiative" || type == "subprogram") {
    return "Programs";
  } else if (type == "person") {
    return "People";
  } else if (type == "event") {
    return "Events";
  } else {
    return "Other Pages";
  }
}

function SearchResultList({results, isFetching, hasNext, hasPrevious, fetchNext, fetchPrevious}) {
  // Remember if we've tried to fetch before
  // This helps us differentiate between the initial state and "No results"
  const [hasFetched, setHasFetched] = useState(false);
  const [fetchingNext, setFetchingNext] = useState(false);
  const [fetchingPrevious, setFetchingPrevious] = useState(false);
  useEffect(() => {
    if (isFetching) {
      setHasFetched(true);
    } else {
      setFetchingNext(false);
      setFetchingPrevious(false);
    }

  }, [isFetching]);

  if (!hasFetched) {
    return <></>;
  }

  if (results.length === 0) {
    // No results, display something to the user to explain why
    if (isFetching) {
      return (
        <div className="program__publications-list-wrapper">
          <div className="program__publications-list margin-top-60">
              <LoadingDots />
          </div>
        </div>
      );
    } else {
      return (
        <h4 className="centered">No results found</h4>
      );
    }
  }

  const onClickNext = e => {
    e.preventDefault();

    setFetchingNext(true);
    fetchNext();
  }

  const onClickPrevious = e => {
    e.preventDefault();

    setFetchingPrevious(true);
    fetchPrevious();
  }

  let emptyGroups = new Set(["Publications", "Programs", "People", "Events", "Other Pages"]);

  return (
    <div className="program__publications-list-wrapper">
      {Array.from(groupBy(results, classifyResult), ([header, subresults]) => {
        emptyGroups.delete(header);
        return (
          <div>
            <h2>{header}</h2>
            <div className="program__publications-list">
              {subresults.map((result, i) => {
                if(result.content_type.api_name == 'person')
                  return ( <Person key={`person-${result.id}`} person={result} /> );
                return ( <PublicationListItem key={`post-${result.id}`} post={result} /> );
              })}
            </div>
          </div>)
      })}
      {[...emptyGroups].map(groupName => {
        return (
          <div>
            <h2>{groupName}</h2>
            <div className="program__publications-list">
              No results.
            </div>
          </div>)
      })}
      {hasPrevious &&
      <div className="program__publications-list-load-more margin-top-10" style={{float: 'left'}}>
        <button className={`button${fetchingPrevious ? ' is-fetching' : ''}`} onClick={onClickPrevious} disabled={isFetching}>
          <span className="load-more-label">Previous</span>
          {fetchingPrevious && <span className="loading-dots--absolute">
            <span>.</span><span>.</span><span>.</span>
          </span>}
        </button>
      </div>}
      {hasNext &&
      <div className="program__publications-list-load-more margin-top-10">
        <button className={`button${fetchingNext ? ' is-fetching' : ''}`} onClick={onClickNext} disabled={isFetching}>
          <span className="load-more-label">Next</span>
          {fetchingNext && <span className="loading-dots--absolute">
            <span>.</span><span>.</span><span>.</span>
          </span>}
        </button>
      </div>}
    </div>
  );
}

export default function Search({location, history}) {
  const {query, ...paginationFilter} = QueryString.parse(location.search);

  const [queryInputValue, setQueryInputValue] = useState(query);
  const [results, setResults] = useState([]);
  const [isFetching, setIsFetching] = useState(false);

  // These contain the value of paginationFilter for the next/previous pages
  // null = next/prev page doesn't exist
  const [nextPaginationFilter, setNextPaginationFilter] = useState(null);
  const [previousPaginationFilter, setPreviousPaginationFilter] = useState(null);

  // Gets query params from state
  const getQueryParams = (query, paginationFilter) => {
    const params = {};

    if (query) {
      params['query'] = query;
    }

    if (paginationFilter) {
      Object.assign(params, paginationFilter);
    }

    if (params) {
      return '?' + QueryString.stringify(params);
    } else {
      return '';
    }
  };

  console.log("RERENDER")

  // Perform search when query changes
  useEffect(() => {
    // Update query input value when user hits back/forward
    setQueryInputValue(query);

    const queryParams = getQueryParams(query, paginationFilter);

    if (query) {
      // Fetch results
      // TODO: Make sure responses come back in correct order
      setIsFetching(true);
      fetch(`/api/search/${queryParams}`)
      .then(response => response.json())
      .then(json => {
        setResults(json.results);
        setIsFetching(false);

        const extractPaginationFilter = url => {
          if (url) {
            const parsedUrl = QueryString.parseUrl(url);
            const {query='', ...paginationFilter} = parsedUrl.query;

            return paginationFilter;
          } else {
            return null;
          }
        }

        setNextPaginationFilter(extractPaginationFilter(json.next));
        setPreviousPaginationFilter(extractPaginationFilter(json.previous));
      });
    } else {
      setIsFetching(false);
      setResults([]);
      setNextPaginationFilter(null);
      setPreviousPaginationFilter(null);
    }
  }, [location.key]);

  // Trigger search when user presses the 'Enter' key
  const onKeyDownInSearchBox = e => {
    if (e.key === 'Enter') {
      history.push({
        pathname: location.pathname,
        search: getQueryParams(queryInputValue, null),
      });
    }
  };

  const onClickSearch = e => {
    e.preventDefault();

    history.push({
      pathname: location.pathname,
      search: getQueryParams(queryInputValue, null),
    });
  };

  const setPaginationFilter = newPaginationFilter => {
    history.push({
      pathname: location.pathname,
      search: getQueryParams(queryInputValue, newPaginationFilter),
    });
  };

  return (
    <div className="home__panels__search container">
      <div className="input margin-bottom-35">
        <input type="text" value={queryInputValue} name="query" onChange={e => setQueryInputValue(e.target.value)} onKeyDown={onKeyDownInSearchBox} required />
        <button className="button--text input__submit with-caret--right" onClick={onClickSearch}>Search</button>
      </div>


      <SearchResultList
        results={results}
        isFetching={isFetching}
        hasNext={!!nextPaginationFilter}
        fetchNext={() => setPaginationFilter(nextPaginationFilter)}
        hasPrevious={!!previousPaginationFilter}
        fetchPrevious={() => setPaginationFilter(previousPaginationFilter)}
      />
    </div>
  );
}
