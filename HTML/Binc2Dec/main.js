var converter = 1; //Binary to Decimal = 1 || Decimal to Binary = 2

function bintoDecimal(){
    converter = 1
    document.getElementById("a-text").innerHTML = "Binary to Decimal";
    document.getElementById("b-text").innerHTML = "Binary:";
    document.getElementById("c-text").innerHTML = "Decimal:";
    document.getElementById("input").placeholder = "Entry a binary number";
}

function decimaltoBin(){
    converter = 2
    document.getElementById("a-text").innerHTML = "Decimal to Binary";
    document.getElementById("b-text").innerHTML = "Decimal:";
    document.getElementById("c-text").innerHTML = "Binary:";
    document.getElementById("input").placeholder = "Entry a Decimal number";
}

function Converter(string) {
    decimal = Number;
    if(converter == 1){
        let decimal = +0;
    let bits = +1;
    for(let i = 0; i < string.length; i++) {
        let currNum = +(string[string.length - i - 1]);
        if(currNum === 1) {
            decimal += bits;
        }
        bits *= 2;
        document.getElementById("output").innerHTML=(decimal);
    }
    }
    if(converter == 2){
        document.getElementById("output").innerHTML=(bits);
    }
  }
  