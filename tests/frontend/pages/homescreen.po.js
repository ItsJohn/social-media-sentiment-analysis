'use strict';

var _ = require('../../../frontend/node_modules/lodash');

function searchScreen() {
      this.textbox = element(by.id('searchTerm'));
      this.button = element(by.id('search_term_button'));
}


_.assign(searchScreen.prototype, {
      loadPage : function() {
            return browser.get('/#!/');
      }
});

module.exports = searchScreen;
