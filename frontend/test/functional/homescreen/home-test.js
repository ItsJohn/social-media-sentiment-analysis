describe('Search term functionality', function() {
      var searchScreen = require('../../pages/homescreen.po.js'),
            search;

      beforeEach(function() {
            search = new searchScreen();
            search.loadPage();
      });

      it('should have a title', function() {
            expect(browser.getTitle()).toEqual('Opinion Mining');
      });
});
