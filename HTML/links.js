class links {
  constructor () {
    this.list = [];
  };

  add (name, link) {
    function helper(arr) {
      if (arr.length < 1) { return [[name,link]]; }
      let curr = arr.shift()
      let b = name.toLowerCase() > curr[0].toLowerCase();
      let output = b ? helper(arr) : arr;
      output.unshift(curr);
      if (!b) {
        output.unshift([name,link]);
      }
      return output;
    };
    this.list = helper(this.list);
  };
  
  listify () {
    let ul = document.createElement("UL");
    for (let each of this.list) {
      let li = document.createElement("LI");
      let a = document.createElement("a");
      a.setAttribute("href",each[1]);
      let txt = document.createTextNode(each[0]);
      a.appendChild(txt);
      li.appendChild(a);
      ul.appendChild(li);
    }
    return ul;
  };

  getList () {
    let out = "";
    for (let each of this.list) {
      out += ", {" + each + "}";
    }
    return "{" + out.slice(2) + "}";
  }
};
