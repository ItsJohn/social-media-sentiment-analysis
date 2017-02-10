exports.config = {
	seleniumServerJar: '../../node_modules/selenium-server-standalone-jar/jar/selenium-server-standalone-3.0.1.jar',
	specs: ['functional/**/*-test.js'],
	seleniumAddress: 'http://127.0.0.1:4444/wd/hub',
	capabilities: {
		'browserName': 'chrome'
	},
	baseUrl: 'http://localhost:8888/#!/'
};
