files.forEach(file => {
    if (path.extname(file) === '.js') {
        let contents = fs.readFileSync(file, 'utf8');
        console.log('Protecting ' + file);

        // Change the settings here  -  https://github.com/javascript-obfuscator/javascript-obfuscator
        let ret = javaScriptObfuscator.obfuscate(contents, {
            compact: true
            , controlFlowFlattening: false
            , controlFlowFlatteningThreshold: 0.75
            , deadCodeInjection: false
            , deadCodeInjectionThreshold: 0.4
            , debugProtection: false
            , debugProtectionInterval: false
            , disableConsoleOutput: false
            , domainLock: []
            , identifierNamesGenerator: 'hexadecimal'
            , identifiersPrefix: ''
            , inputFileName: ''
            , log: false
            , renameGlobals: false
            , reservedNames: []
            , reservedStrings: []}