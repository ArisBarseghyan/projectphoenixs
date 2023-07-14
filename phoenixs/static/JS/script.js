let panels = document.querySelectorAll(".panel");
let fronts = document.querySelectorAll(".front");
let backs = document.querySelectorAll(".back");
let replay_btn = document.querySelector(".replay");

const mirrorTL = gsap.timeline();
const titleTL = gsap.timeline();

gsap.set(replay_btn, { opacity: 0 });
replay_btn.addEventListener("click", (e) => {
	mirrorTL.restart();
	titleTL.restart();
	gsap.to(e.target, 0.5, { opacity: 0 });
	console.log(e.target);
});

mirrorTL
	.to(fronts, 2.5, { backgroundPosition: "30px 0px", ease: "expo.inOut" })
	.to(panels, 2.5, { z: -300, rotationY: 180, ease: "expo.inOut" }, "-=2.3")
	.from(
		backs,
		2.5,
		{
			backgroundPosition: "-30px 0px",
			ease: "expo.inOut",
			onComplete: () => {
				gsap.to(replay_btn, 1, { opacity: 1 });
			}
		},
		"-=2.3"
	);

titleTL
	.to(".layer", 1, { clipPath: "polygon(3% 0, 100% 0%, 100% 100%, 0% 100%" })
	.to(".layer h1", 2, { x: 400, ease: "expo.inOut" }, "-=0.5")
	.to(".cta", 2, { x: 0, ease: "expo.inOut" }, "-=2");
var myInput = document.getElementById("psw");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
}

  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }

  // Validate length
  if(myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}
