document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".rst-content dl dt").forEach(function (el) {
      const text = el.textContent.trim();
      if (text.endsWith(" :") || text.endsWith(") :") || text.endsWith("(1x1 dictionary)")) { 
        el.classList.add("not_bold");
      }
    });
  });
  

  