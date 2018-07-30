var FontMultiplier = 0.0;
var FontSteps = 0.1
var CurrentSlide = 0;
var slides = document.getElementsByTagName("section");
var n = slides.length;

function draw() {
  slides[CurrentSlide].style.opacity = 0;
  FontMultiplier = 0.0;
  document.documentElement.style.setProperty("--font_multiplier", FontMultiplier);
  while (slides[CurrentSlide].clientHeight < document.body.clientHeight) {
    FontMultiplier += FontSteps
    document.documentElement.style.setProperty("--font_multiplier", FontMultiplier);
  }
  FontMultiplier -= FontSteps
  document.documentElement.style.setProperty("--font_multiplier", FontMultiplier);

  slides[CurrentSlide].style.opacity = 1;
}

function PassSlide(inc) {
  slides[CurrentSlide].style.display = "none";
  CurrentSlide += inc;
  if (CurrentSlide > n - 1) {
    CurrentSlide = 0
  };
  if (CurrentSlide < 0) {
    CurrentSlide = n - 1
  };
  slides[CurrentSlide].style.display = "block";
}

for (i = 0; i < n; i++) {
  slides[i].style.display = "none";
}
slides[CurrentSlide].style.display = "block";
draw()

window.onresize = function() {
  draw()
};

document.onkeydown = function(e) {
  if (e.key == 'ArrowRight' || e.key == 'Enter' || e.key == ' ') {
    PassSlide(1)
    draw()
  }
  if (e.key == 'ArrowLeft') {
    PassSlide(-1)
    draw()
  }
};

window.onbeforeprint = function() {
  for (i = 0; i < n; i++) {
    slides[i].style.display = "block";
  }
};

window.onafterprint = function() {
  for (i = 0; i < n; i++) {
    slides[i].style.display = "none";
  }
  slides[CurrentSlide].style.display = "block";
};

var l_div = document.createElement("div");
l_div.style.zIndex = 2;
l_div.className = 'btn';
l_div.style.position = "fixed";
l_div.style.background = "black";
l_div.style.opacity = "0.0";
l_div.style.top = '0px';
l_div.style.left = '0px';
l_div.style.width = "3%";
l_div.style.height = "100%";
l_div.onmouseenter = function(e) {
  l_div.style.opacity = "0.5";
  l_div.style.width = "10%";
}
l_div.onmouseleave = function(e) {
  l_div.style.opacity = "0.0";
  l_div.style.width = "3%";
}
l_div.onmousedown = function(e) {
  PassSlide(-1);
  draw();
}
document.body.appendChild(l_div);


var r_div = document.createElement("div");
r_div.style.zIndex = 2;
r_div.className = 'btn';
r_div.style.position = "fixed";
r_div.style.background = "black";
r_div.style.opacity = "0.0";
r_div.style.top = '0px';
r_div.style.left = '97%';
r_div.style.width = "3%";
r_div.style.height = "100%";
r_div.onmouseenter = function(e) {
  r_div.style.opacity = "0.5";
  r_div.style.left = '90%';
  r_div.style.width = "10%";
}
r_div.onmouseleave = function(e) {
  r_div.style.opacity = "0.0";
  r_div.style.left = '97%';
  r_div.style.width = "3%";
}
r_div.onmousedown = function(e) {
  PassSlide(+1);
  draw();
}
document.body.appendChild(r_div);