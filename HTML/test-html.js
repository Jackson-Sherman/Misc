function randgen(){
    return Math.floor(Math.random() * 60) / 60;
};

function hsv(kore) {
    document.getElementById("cuerpo").innerHTML = "";
    gridthem(kore);
};

function hsv1(esto) {
    var cuerpo = document.getElementById("cuerpo");
    var newDiv = document.createElement("DIV");
    

    var rand = randgen();
    var color = hsv_to_hex(rand);

    var text = rand.toString();
    text += ' => "';
    text += color.toString();
    text += '"';

    newDiv.innerHTML += text;
    
    newDiv.style.backgroundColor = color;

    cuerpo.appendChild(newDiv);
};

function hsv2(esto) {
    //Only on first click:
    if (document.getElementById("cuerpo").innerHTML == "") {
        let mesa = document.createElement("TABLE");
            mesa.id = "mesa";
            let newTR = document.createElement("TR");
                let newTD = document.createElement("TD");
                    newTD.style.backgroundColor = hsv_to_hex(randgen());
                newTR.appendChild(newTD);
            mesa.appendChild(newTR);
        document.getElementById("cuerpo").appendChild(mesa);
    }
    else {
        var mesa = document.getElementById("mesa");
        
        for (let i = 0; i < document.querySelectorAll("#mesa tr").length; i++) {
            if (i === 0) {
                let newTR = document.createElement("TR");
                mesa.appendChild(newTR);
            }
            else {
                let newTD = document.createElement("TD");
                newTD.style.backgroundColor = hsv_to_hex(randgen());
                document.querySelectorAll("#mesa tr")[document.querySelectorAll("#mesa tr").length - 1].appendChild(newTD);
            }

            let newTD = document.createElement("TD");
            newTD.style.backgroundColor = hsv_to_hex(randgen());
            document.querySelectorAll("#mesa tr")[i].appendChild(newTD);
        }
    }
};

function listthem(esto){
    if(document.getElementById("cuerpo").innerHTML == ""){
        var mesa = document.createElement("TABLE");
        mesa.id = "mesa";

        for(let i = 0; i < 60; i++){
            let newtr = document.createElement("TR");
    
            for(let j = 0; j < 1; j++){
                let newtd = document.createElement("TD");
    
                if (j === 0) {
                    str = i.toString();
                    newtd.innerHTML = (str.length < 2) ? "0" + str : str;
                    newtd.style.backgroundColor = hsv_to_hex(i / 60);
                }
                newtr.appendChild(newtd);
            }
            mesa.appendChild(newtr);
        }
        document.getElementById("cuerpo").appendChild(mesa);
    }
    else{
        let trs = document.querySelectorAll("#mesa tr");
        let cuanto = trs[0].children.length + 1;
        for(let i = 0; i < trs.length; i++){
            let newtd = document.createElement("TD");
            let num = ((i * cuanto) % 60);
            let str = num.toString();

            while (str.length < 2) {
                str = "0" + str;
            }

            newtd.style.backgroundColor = hsv_to_hex(num / 60);
            newtd.innerHTML = str;
            trs[i].appendChild(newtd);
        };
    }
    
};

function gridthem(esto){
    var vals = [];

    for (let y = 0; y < 60; y++) {
        vals.push([]);

        for (let x = 0; x < 60; x++) {
            vals[y].push({
                mod: y * x % 60,
                border: {
                    right: Boolean(y * (x + 1) % 60 < y * x % 60),
                    bottom: Boolean((y + 1) * x % 60 < y * x % 60)
                }
            });
        }
    }

    var mesa = document.createElement("TABLE");
    mesa.id = "mesa";

    
    for(let y = 0; y < 60; y ++){
        let newtr = document.createElement("TR");

        for(let x = 0; x < 60; x++){
            let newtd = document.createElement("TD");
            let num = vals[y][x].mod;

            if(document.getElementById("number?").checked){
                let str = num.toString();
                while (str.length < 2) {
                    str = "0" + str;
                }
                newtd.innerHTML = str;
            }

            if(document.getElementById("color?").checked){
                newtd.style.backgroundColor = hsv_to_hex(num / 60);
            }
            
            if(document.getElementById("border?").checked){
                if(vals[y][x].border.right){
                    newtd.style.borderRight = "1px solid black";
                }
                if(vals[y][x].border.bottom){
                    newtd.style.borderBottom = "1px solid black";
                }
            }

            newtr.appendChild(newtd);
        }
        mesa.appendChild(newtr);
    }
    document.getElementById("cuerpo").appendChild(mesa);
};