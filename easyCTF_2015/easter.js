__=("")['constructor']['fromCharCode'];

("")['constructor']['constructor'](if (window.addEventListener) {
    var index = 0;
    var konami = [38,38,40,40,37,39,37,39,66,65,13];

    window.addEventListener("keydown", function(e){
        if (e.keyCode === konami[index])
        {
            index++; //valid key at the valid point

            if (index == konami.length)
            {
                document.getElementById("valerie").innerHTML="01111011011011010110100101110011011100110110100101101111011011100111001101110101011000110110001101100101011100110111001101111101";
            }
        } else {
            // incorrect code restart
            index = 0;
        }
   });
})();
