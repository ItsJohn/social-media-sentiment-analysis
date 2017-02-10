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
      // it('should send text to the textbox', function() {
            // search.textbox.sendKeys('hello world, Donald');
            // search.button.click();
            // expect(browser.getCurrentUrl()).toEqual('http://localhost:8888/#!/analysis')
      // })
});
