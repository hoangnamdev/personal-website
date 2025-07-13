const addEventOnElements = function (elements, eventType, callback) {
    for (let i = 0, len = elements.length; i < len; i++) {
      elements[i].addEventListener(eventType, callback);
    }
}

let i = 0

function update(e){
    const circle = document.getElementById("cursor");
    if (i == 0) {
        cursor.style.display = "block";
    }
    let width = circle.offsetWidth;
    let height = circle.offsetHeight;

    var x = e.clientX || e.touches[0].clientX
    var y = e.clientY || e.touches[0].clientY

    document.documentElement.style.setProperty('--cursorX', (x - (width / 2)) + 'px')
    document.documentElement.style.setProperty('--cursorY', (y - (height / 2)) + 'px')
}
document.addEventListener('mousemove',update)
document.addEventListener('touchmove',update)

let cursor = document.getElementById("cursor");
let hoverElements = [...document.querySelectorAll("a"), ...document.querySelectorAll("button")];

addEventOnElements(hoverElements, "mouseover", function () {
    cursor.classList.add("hovered");
});
  
addEventOnElements(hoverElements, "mouseout", function () {
    cursor.classList.remove("hovered");
});

var TxtType = function(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
};

TxtType.prototype.tick = function() {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];

    if (this.isDeleting) {
    this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
    this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

    var that = this;
    var delta = 200 - Math.random() * 100;

    if (this.isDeleting) { delta /= 2; }

    if (!this.isDeleting && this.txt === fullTxt) {
    delta = this.period;
    this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
    this.isDeleting = false;
    this.loopNum++;
    delta = 500;
    }

    setTimeout(function() {
    that.tick();
    }, delta);
};

window.onload = function() {
    var elements = document.getElementsByClassName('typing');
    for (var i=0; i<elements.length; i++) {
        var toRotate = elements[i].getAttribute('data-type');
        var period = elements[i].getAttribute('data-period');
        if (toRotate) {
          new TxtType(elements[i], JSON.parse(toRotate), period);
        }
    }
    // INJECT CSS
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".typing > .wrap { border-right: 0.08em solid #fff}";
    document.body.appendChild(css);
};

var header_circle = document.getElementsByClassName("header__circle")
var colors = ['#822e00', '#827300', '#298200', '#008282', '#000f82', '#520082', '#000f82', '#008277', '#008207', '#808200', '#823f00', '#820700'];
var currentIndex = 0;
setInterval(function () {
    document.documentElement.style.setProperty('--animcircle', colors[currentIndex])
    if (!colors[currentIndex]) {
        currentIndex = 0;
        document.documentElement.style.setProperty('--animcircle', colors[currentIndex])
    } else {
        currentIndex++;
    }
}, 1750);

var coll = document.getElementsByClassName("nav__box");
var content = document.getElementsByClassName("nav__links");

var clickfade = function fade() {
    console.log("heya")
    content[0].style.opacity = "0";
    content[0].style.top = "-100vw";
}

if (getComputedStyle(coll[0]).getPropertyValue("display") === "block") {
    content[0].addEventListener("click", clickfade);
}

coll[0].addEventListener("click", function() {
    if (content[0].style.opacity === "1") {
        content[0].style.opacity = "0";
        content[0].style.top = "-100vw";
    } 
    else {
        content[0].style.opacity = "1";
        content[0].style.top = "14vw";
    }
})

window.addEventListener("resize", function() {
    if (window.innerWidth > 450) {
        content[0].removeEventListener("click", clickfade);
        content[0].style.opacity = "1";
        content[0].style.top = "0";
    }
    else {
        content[0].addEventListener("click", clickfade);
        content[0].style.opacity = "0";
        content[0].style.top = "-100vw";
    }
})