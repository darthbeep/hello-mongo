var meteorites = []

function populate_metiorites() {
    //var data2 = data.replace(/u'(?=[^:]+')/g, "\"");
    //console.log(data2);
    //find_something('Aachen', 'name');
    findall();
}

function setup_Vue() {
    Vue.component('meteor', {
        props: ['name', 'date'],
        template: '<div onmouseover=\"find_something(this.innerHTML,\'name\')\">{{ name }}</div>'
    })

    var app = new Vue({
        el: "#app",
        data: {
            'mets': meteorites,
            'info': {
                "name": "",
                "fall": "",
                "year": ""
            }
        }
    })
}


function find_something(thing, term) {
    console.log('find start');
    //You guys kept telling me I use too much jQuery. So I'm going jQuery-less
    //Doesn't work on IE.
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/find");
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            updateInfo(xhr.responseText);
        }
        else {
            console.log("nope");
        }

    }
    xhr.send(encodeURI('find='+thing +"&term=" +term));
}

function findall() {
    console.log('find start');
    //You guys kept telling me I use too much jQuery. So I'm going jQuery-less
    //Doesn't work on IE.
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/findall");
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            meteorites = JSON.parse(xhr.responseText);
            setup_Vue();
        }
        else {
            console.log("nope");
        }

    }
    xhr.send();
}

function updateInfo(stuff) {
    js = JSON.parse(stuff);
    var st = "Name: " + js.name;
    st += "<br>Year: " + js.year;
    st += "<br>Reclat: " + js.reclat + ", reclong: " + js.reclong;
    st += "<br>Mass: " + js.mass;
    document.getElementById("info").innerHTML = st;
}
