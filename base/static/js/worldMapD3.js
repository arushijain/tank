var basic_choropleth = new Datamap({
  element: document.getElementById("container"),
  projection: 'mercator',
   height: null, //if not null, datamaps will grab the height of 'element'
    width: null, //if not null, datamaps will grab the width of 'element'
  fills: {
    defaultFill: "#ABDDA4",
    authorHasTraveledTo: "#fa0fa0"
  },
  data: {
    USA: { fillKey: "authorHasTraveledTo" },
    JPN: { fillKey: "authorHasTraveledTo" },
    ITA: { fillKey: "authorHasTraveledTo" },
    CRI: { fillKey: "authorHasTraveledTo" },
    KOR: { fillKey: "authorHasTraveledTo" },
    DEU: { fillKey: "authorHasTraveledTo" },
  }
});

var colors = d3.scale.category10();

// window.setInterval(function() {
//   basic_choropleth.updateChoropleth({
//     USA: colors(Math.random() * 10),
//     RUS: colors(Math.random() * 100),
//     AUS: { fillKey: 'authorHasTraveledTo' },
//     BRA: colors(Math.random() * 50),
//     CAN: colors(Math.random() * 50),
//     ZAF: colors(Math.random() * 50),
//     IND: colors(Math.random() * 50),
//   });
// }, 2000);

$(".dropdown-menu li a").click(function(){
  var selText = $(this).text();
  $(this).parents('.dropdown').find('.dropdown-toggle').html(selText+' <span class="caret"></span>');
  var form = document.getElementById("sendData");
  var id = $(this).parents('.dropdown-menu').attr("id");
  console.log(id);
  form.elements[id].value = selText;
  });


document.addEventListener('click', function(e) {

    e = e || window.event;
    var target = e.target || e.srcElement;

    if(target.className['baseVal'] != null){
    //getting the country code
      var countryClass = target.className['baseVal'];
      var countryCode = countryClass.split(" ")[1];
      var countryName =  target.getAttribute("name");
      var form = document.getElementById("sendData");
      form.elements["country"].value = countryName;
      var options = $(".dropdown-toggle");
      console.log("options");
      console.log(options);
      console.log(options[0].class);
      form.elements["genre"].value = $("#genreSelect").text();
      form.elements["type"].value = $("#typeSelect").text();
      form.elements["license"].value = $("#licenseSelect").text();
      form.submit();

      $.post(
        "world",
      //  {'countryId':countryCode,'countryName':countryName},
        function(data){
            alert("Data Loaded: " + data);}
        );
    } 

}, false);
