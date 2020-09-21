function hsv_to_hex(hue){
    hue %= 1;
    hue *= 6;
    color=[0,0,0]
    if(hue < 1) {
        hue %= 1;
        color = [1, hue, 0];
    } else if(hue < 2) {
        hue %= 1;
        color = [1 - hue, 1, 0];
    } else if(hue < 3) {
        hue %= 1;
        color = [0, 1, hue];
    } else if(hue < 4) {
        hue %= 1;
        color = [0, 1 - hue, 1];
    } else if(hue < 5) {
        hue %= 1;
        color = [hue, 0, 1];
    } else {
        hue %= 1;
        color = [1, 0, 1 - hue];
    }

    output = "#"

    for(var i = 0; i < color.length; i++){
        color[i] *= 256;
        color[i] = Math.floor(color[i]);
        if (255 < color[i]){
            color[i] = 255;
        }
        out = color[i].toString(16);
        while (out.length < 2) {
            out = "0" + out;
        }
        output += out;
    }

    return output;
};