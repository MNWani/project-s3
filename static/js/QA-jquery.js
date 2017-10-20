$(document).ready(function() {
  $("#automplete-2").autocomplete({
        source: [
             { value: "ESO Morrowind DLC Guide", url: '/QA_blog/qa_corner/#videocontainer1' }, 
             { value: "The Witcher III: Wild Hunt Guide", url: '/QA_blog/qa_corner/#videocontainer2' },
             { value: "Destiny 2 Guide", url: '/QA_blog/qa_corner/#videocontainer3' },
             { value: "Legend of Zelda: BOW Guide", url: '/QA_blog/qa_corner/#videocontainer4' },
             { value: "Fifa 18 Guide", url: '/QA_blog/qa_corner/#videocontainer5' },
        ],
        select: function (event, ui) {
            window.location = ui.item.url;
        }
    });

  $("#newssubscribe").click(function(){
    alert("Thank you for subscribing.");
});

});




 