let i = 0
const circle = document.getElementById("cursor");

function update(e){
    if (i == 0) {
        cursor.style.opacity = "1";
    }

    var x = e.clientX || e.touches[0].clientX
    var y = e.clientY || e.touches[0].clientY

    circle.animate({
        left: `${x}px`,
        top: `${y}px`
    }, { duration: 3000, fill: "forwards" });
}
document.addEventListener('mousemove',update)
document.addEventListener('touchmove',update)

let hoverElements = [...document.querySelectorAll("a"), ...document.querySelectorAll("button")];

addEventOnElements(hoverElements, "mouseover", function () {
    circle.classList.add("hovered");
});
  
addEventOnElements(hoverElements, "mouseout", function () {
    circle.classList.remove("hovered");
});