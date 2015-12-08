document.getElementById("panel").onclick = function() {
    document.getElementById("message").innerHTML = "Checking...";
    setTimeout(function() {
	try {
            
	    if (location.search.length != 25) throw Error();
            
            // query: location.search.substring(1).split(/{|}/);
            
            var query = ['flag', '$z$e$P$t$@$b$a$qu$$$$$$$$', ''];
            
	    // flag format: flag{xxxxxxxxxxxxxxxxxx}
      
	    var message = ['The', 'flag', 'is', 'a', 'string.'];
      
	    var query2 = query[1].split("$");
      
	    if (query2[8].split("").map(function(k) { return k.charCodeAt(0); }).reduce(function(x, y) { return x + Math.pow(y ^ 95, 4); }) != 3111809) // 3111809 = 113 + Math.pow(117 ^ 95, 4), q = chr(117), u = chr(95)
                throw Error();
            /*
            for (var i in message) {
                if (i) {
                    var q = message.splice(i, 1).join("");
                    var h = CryptoJS.MD5(message.splice(i + 1).join("") + message.join("%"));
                    var z = h.toString() + h.words.splice(0, 1); break;
                }
            }
            */
            var q = 'The';
            var h = CryptoJS.MD5('isastring.flag');
            var z = '1dca6335fecd41464f142fbfa1a56b0f499802933';
      
            var funcs = [ String.fromCharCode,
                          Object.getOwnPropertyNames,
                          function(x) {
                              return (x == 'e') ? 3 : x;
                          },
                          function(c) {
                              return [ query2[4],
                                       156,
                                       230,
                                       query2[6].charCodeAt(0) * 2 ].reduce(c);
                          }
                        ];
	    var m = new MersenneTwister(4744);

	    var string = [
                "r3v3rse",
                
                funcs[3](function(m, n) {
                    return m + String.fromCharCode(n ^ h.words.splice(0, 1));
                }), // must equal th1s
                
                [ 181, 78, 28, query2[0].charCodeAt(0),225, 129 ].map(function(x) {
                    return String.fromCharCode(((m.genrand_int32() * Math.sqrt(m.random())) & 0xff) ^ x);
                }).join("") // must equal str1ng
            ].join(String.fromCharCode(query2[3].charCodeAt(0) + 0xF)); // must be _, so query2[3] = P
            
	    if (string == 'r3v3rse_th1s_str1ng') {
		document.getElementById("message").innerHTML = "Correct!";
	    } else {
		throw Error();
	    }
	} catch (e) {
	    document.getElementById("message").innerHTML = "Nope. :(";
	}
    }, 1000);
};
