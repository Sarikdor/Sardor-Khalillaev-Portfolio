const accordionButtons = document.body.querySelectorAll(".accordion-button");

accordionButtons.forEach((accordionButton) => {
  accordionButton.addEventListener("click", () => {
    accordionButton.children[1].classList.toggle("fa-plus")
    accordionButton.children[1].classList.toggle("fa-minus")
    accordionButton.nextElementSibling.classList.toggle("accordion-show");
    
  });
});
