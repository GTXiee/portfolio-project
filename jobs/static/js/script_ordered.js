var inputList;

document.getElementById('btn-process').addEventListener('click', function(){
    // read input as array
    var input = document.getElementById('input-text-1').value.trim();
    inputList = input.split('\n');

    // read checkbox input
    var broadChecked = document.getElementById('broad-checkbox').checked;
    var phraseChecked = document.getElementById('phrase-checkbox').checked;
    var exactChecked = document.getElementById('exact-checkbox').checked;
    var bmmChecked = document.getElementById('bmm-checkbox').checked;


    // output
    var outputArr = [];

    if (broadChecked) {
        outputArr.push(inputList);
    } 
    if (phraseChecked) {
        var phraseArr = [];
        for (var i=0; i<inputList.length; i++) {
            phraseArr.push('"' + inputList[i].trim() + '"');
        }
        outputArr.push(phraseArr);
    }
    if (exactChecked) {
        var exactArr = [];
        for (var i=0; i<inputList.length; i++) {
            exactArr.push('[' + inputList[i].trim() + ']');
        }
        outputArr.push(exactArr);
    }
    if (bmmChecked) {
        var bmmArr = [];
        for (var i=0; i<inputList.length; i++) {
            var line = inputList[i].trim();
            var newLine = '+' + line.split(' ').join(' +');
            bmmArr.push(newLine);
        }
        outputArr.push(bmmArr);
    }
    
    console.log(outputArr);
    
    var finalArr = [];
    for (var i=0; i<inputList.length; i++) {
        for (var j=0; j<outputArr.length; j++) {
            finalArr.push(outputArr[j][i])
        }
    }

    document.getElementById('output-text').value = finalArr.join('\n');
});

// add copy function to text
document.getElementById('btn-copy').addEventListener('click', copyText);

// copies output to keyboard
function copyText() {
    let copyText = document.getElementById('output-text');
    copyText.select();
    document.execCommand('copy');
    alert('Copied to clipboard');
}