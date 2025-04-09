document.querySelectorAll('.box').forEach(box => {
    box.addEventListener('click', () => {
      box.classList.remove('animate'); // reset if already animated
      void box.offsetWidth; // force reflow to restart animation
      box.classList.add('animate');
    });
  });
  