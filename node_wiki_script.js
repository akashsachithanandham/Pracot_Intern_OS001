console.log("Hello !! ")
if(process.argv.length == 2){
    const prompt = require('prompt-sync')();
    
    const queryName = prompt('Enter the Query: ');

    const logFile = prompt('Enter the log file name: ')

    const wikiLink = "https://en.wikipedia.org/wiki/" + queryName + '\n';
    console.log('wikipedia link',wikiLink);
    var fs = require('fs');

    fs.appendFile(logFile, wikiLink, function (err) {
    if (err) throw err;
    console.log('Saved!');
    });
    fs.close();
}
else{
    const queryName = process.argv[2]

    const logFile = process.argv[3]

    const wikiLink = "https://en.wikipedia.org/wiki/" + queryName + '\n';
    console.log('wikipedia link',wikiLink);
    var fs = require('fs');

    fs.appendFile(logFile, wikiLink, function (err) {
    if (err) throw err;
    console.log('Saved!');
    });
    fs.close();
}

