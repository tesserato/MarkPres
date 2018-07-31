/* <><><><> GLOBAL VARS <><><><> */
var loading = document.getElementById("splash");
var FontSteps = 0.1;
var printing = false;
var CurrentSlide = 0;
var slides = document.getElementsByTagName("section");
var n = slides.length;


/* <><><><> FUNCTIONS <><><><> */

function recalculate(){
  console.log('recalculate');
  for (i = 0; i < n; i++) {
    slides[i].style.display = "block";
    FontMultiplier = 0.0;
    document.documentElement.style.setProperty("--font_multiplier_" + i, FontMultiplier);
    while (slides[i].clientHeight < window.innerHeight * 0.90){
      FontMultiplier += FontSteps
      document.documentElement.style.setProperty("--font_multiplier_" + i, FontMultiplier);
    }
    FontMultiplier -= FontSteps
    document.documentElement.style.setProperty("--font_multiplier_" + i, FontMultiplier);
    slides[i].style.display = "none";
  }
  slides[CurrentSlide].style.display = "block";
}

function PassSlide(inc){
  slides[CurrentSlide].style.display = "none";
  CurrentSlide += inc;
  if (CurrentSlide > n - 1) {CurrentSlide = 0};
  if (CurrentSlide < 0) {CurrentSlide = n - 1};
  slides[CurrentSlide].style.display = "block";
}


/* <><><><> CREATING DOM ELEMENTS <><><><> */


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
l_div.onmouseenter = function(e){
  l_div.style.opacity = "0.5";
  l_div.style.width = "10%";
}
l_div.onmouseleave = function(e){
  l_div.style.opacity = "0.0";
  l_div.style.width = "3%";
}
l_div.onmousedown = function(e){
  PassSlide(-1);
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
r_div.onmouseenter = function(e){
  r_div.style.opacity = "0.5";
  r_div.style.left = '90%';
  r_div.style.width = "10%";
}
r_div.onmouseleave = function(e){
  r_div.style.opacity = "0.0";
  r_div.style.left = '97%';
  r_div.style.width = "3%";
}
r_div.onmousedown = function(e){
  PassSlide(+1);
}
document.body.appendChild(r_div);


/* <><><><> EVENTS <><><><> */

window.onresize = function(){
  console.log('onresize');
  if (printing == false){
    recalculate();
    }
}

window.onload = function(){
  console.log('onload');
  recalculate();
  loading.style.visibility = "hidden";
}

document.onkeydown = function(e){
  if (e.key=='ArrowRight'|| e.key=='Enter'|| e.key==' ') {
    PassSlide(1)
  }
  if (e.key=='ArrowLeft') {
    PassSlide(-1)
  }
}

window.onbeforeprint = function() {
  console.log('onbeforeprint');
  printing = true;
  for (i = 0; i < n; i++) {
    slides[i].style.display = "block";
    // slides[i].clientWidth = 842;
    FontMultiplier = 0.0;
    document.documentElement.style.setProperty("--font_multiplier_" + i, FontMultiplier);
    while (slides[i].clientHeight < (210 + 2) * 96 / 25.4) {
      FontMultiplier += 0.1
      document.documentElement.style.setProperty("--font_multiplier_" + i, FontMultiplier);
    }
    FontMultiplier -= FontSteps
    document.documentElement.style.setProperty("--font_multiplier_" + i, FontMultiplier);
  }
};

window.onafterprint = function() {
  console.log('onafterprint');
  printing = false;
  recalculate();
  for (i = 0; i < n; i++) {
    slides[i].style.display = "none";
  }
  slides[CurrentSlide].style.display = "block";
};