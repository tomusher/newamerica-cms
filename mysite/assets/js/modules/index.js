/*

Exports mapped object of all module functions, called in assets/mysite.js

*/
export default [
  'border-panel',
  'sidemenu',
  'weekly-sidemenu',
  'post-body',
  'mobile-menu',
  'subscribe',
  'picture-grid',
  'search',
  'header',
  'content-controls',
  'fixed-banner',
  'story-excerpt-ellipsis'
].map((moduleName) => require(`./${moduleName}/index.js`).default);
