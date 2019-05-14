var inputListFinal;

document.getElementById('btn-process').addEventListener('click', function () {
    // read inputs depending on combination box
    let combo = document.getElementById('combination-select').value;
    console.log("Value: " + combo);
    let inputLists = [];

    let input1 = document.getElementById('input-text-1').value.trim();
    inputLists.push(input1.split('\n'));
    if (parseInt(combo) > 1) {
        let input2 = document.getElementById('input-text-2').value.trim();
        inputLists.push(input2.split('\n'));
    }
    if (parseInt(combo) === 3) {
        let input3 = document.getElementById('input-text-3').value.trim();
        inputLists.push(input3.split('\n'));
    }

    console.log('inputLists:');
    console.log(inputLists);
    // concatenate the inputs
    let inputListFinal = [];

    switch (combo) {
        case '1':
            inputListFinal = inputLists[0];
            break;
        case '2':
            for (let i = 0; i < inputLists[0].length; i++) {
                for (let j = 0; j < inputLists[1].length; j++) {
                    inputListFinal.push(inputLists[0][i] + " " + inputLists[1][j])
                }
            }
            break;
        case '3':
            for (let i = 0; i < inputLists[0].length; i++) {
                for (let j = 0; j < inputLists[1].length; j++) {
                    for (let k = 0; k < inputLists[2].length; k++) {
                        inputListFinal.push(inputLists[0][i] + " " + inputLists[1][j] + " " + inputLists[2][k])
                    }
                }
            }
    }

    console.log(inputListFinal);


    // read checkbox input
    let broadChecked = document.getElementById('broad-checkbox').checked;
    let phraseChecked = document.getElementById('phrase-checkbox').checked;
    let exactChecked = document.getElementById('exact-checkbox').checked;
    let bmmChecked = document.getElementById('bmm-checkbox').checked;

    // output
    let outputArr = [];
    console.log(inputListFinal);

    if (broadChecked) {
        outputArr.push(inputListFinal);
    }
    if (phraseChecked) {
        var phraseArr = [];
        for (var i = 0; i < inputListFinal.length; i++) {
            phraseArr.push('"' + inputListFinal[i].trim() + '"');
        }
        outputArr.push(phraseArr);
    }
    if (exactChecked) {
        var exactArr = [];
        for (var i = 0; i < inputListFinal.length; i++) {
            exactArr.push('[' + inputListFinal[i].trim() + ']');
        }
        outputArr.push(exactArr);
    }
    if (bmmChecked) {
        var bmmArr = [];
        for (var i = 0; i < inputListFinal.length; i++) {
            var line = inputListFinal[i].trim();
            var newLine = '+' + line.split(' ').join(' +');
            bmmArr.push(newLine);
        }
        outputArr.push(bmmArr);
    }

    console.log(outputArr);

    var finalArr = [];
    for (var i = 0; i < inputListFinal.length; i++) {
        for (var j = 0; j < outputArr.length; j++) {
            finalArr.push(outputArr[j][i])
        }
    }

    document.getElementById('output-text').value = finalArr.join('\n');
});

// add copy function to text
document.getElementById('btn-copy').addEventListener('click', copyText);

// combination boxes
document.getElementById('combination-select').addEventListener('change', function () {
    let chosen = document.getElementById('combination-select').value;
    let inputCol2 = document.getElementById('kw-col-2');
    let inputCol3 = document.getElementById('kw-col-3');
    switch (chosen) {
        case '1':
            inputCol2.style.display = 'none';
            inputCol3.style.display = 'none';
            break;
        case '2':
            inputCol2.style.display = 'inline-block';
            inputCol3.style.display = 'none';
            break;
        case '3':
            inputCol2.style.display = 'inline-block';
            inputCol3.style.display = 'inline-block';
            break;
    }
});

// copies output to keyboard
function copyText() {
    let copyText = document.getElementById('output-text');
    copyText.select();
    document.execCommand('copy');
    alert('Copied to clipboard');
}