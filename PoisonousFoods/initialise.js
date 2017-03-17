var descriptionDict = {
  lead: 'Lead poisoning is a type of metal poisoning caused by lead in the body. The brain is the most sensitive. Symptoms may include abdominal pain, constipation, headaches, irritability, memory problems, inability to have children, and tingling in the hands and feet. It causes almost 10% of intellectual disability of otherwise unknown cause and can result in behavioral problems. Some of the effects are permanent. In severe cases anemia, seizures, coma, or death may occur [7]. Safety limit is five micrograms per deciliter[8].',
  cadmium: 'Cadmium is an extremely toxic metal commonly found in industrial workplaces. Due to its low permissible exposure limit, overexposures may occur even in situations where trace quantities of cadmium are found. Cadmium is used extensively in electroplating, although the nature of the operation does not generally lead to overexposures. Cadmium is also found in some industrial paints and may represent a hazard when sprayed. Operations involving removal of cadmium paints by scraping or blasting may pose a significant hazard [5]. Safety limit is 1 x 10^-3 mg/kg/day[6]. ',
  arsenic: 'Arsenic poisoning is a medical condition that occurs due to elevated levels of arsenic in the body. If exposure occurs over a brief period of time symptoms may include vomiting, abdominal pain, encephalopathy, and watery diarrhea that contains blood. Long-term exposure can result in thickening of the skin, darker skin, abdominal pain, diarrhea, heart disease, numbness, and cancer[3]. Safety limits are 0.5-2 parts per million[4].'
}
function initialise(data, svg) {

  // Add radio buttons
  var w= 285;
  var h= 210;
  var radioButtonsSvg = d3.select("#radio-buttons")
  .append("svg")
  .attr("width", w)
  .attr("height", h)

  //backdrop of color

  //text that the radio button will toggle
  var number= radioButtonsSvg.append("text")
                  .attr("id","numberToggle")
                  .attr("x",0)
                  .attr("y",200)
                  .attr("fill","green")
                  .attr("font-size",14)

  var des = d3.select('#descriptions').append("text")
            .attr('id', 'des')
            .attr('x', 10)
            .text('Click on one of the options to get its description...')


  //container for all buttons
  var allButtons= radioButtonsSvg.append("g")
                      .attr("id","allButtons")

  //fontawesome button labels
  var labels= ['\uf017','\uf200','\uf183'];
  var labels = nutrients;
  //colors for different button states
  var defaultColor= "#6C7A89"
  var hoverColor= "#798795"
  var pressedColor= "#95a1ac"

  //groups for each button (which will hold a rect and text)
  var buttonGroups= allButtons.selectAll("g.button")
                          .data(labels)
                          .enter()
                          .append("g")
                          .attr("class","button")
                          .style("cursor","pointer")
                          .on("click",function(d,i) {
                              updateButtonColors(d3.select(this), d3.select(this.parentNode))
                              var targetid = nutrients[i];
                              selected_nutrient = targetid;
                              d3.select("#descriptions").text(descriptionDict[targetid])
                              d3.selectAll(".force-scale-node").remove();
                              getScale(data, svg, targetid);

                          })
                          .on("mouseover", function() {
                              if (d3.select(this).select("rect").attr("fill") != pressedColor) {
                                  d3.select(this)
                                      .select("rect")
                                      .attr("fill",hoverColor);
                              }
                          })
                          .on("mouseout", function() {
                              if (d3.select(this).select("rect").attr("fill") != pressedColor) {
                                  d3.select(this)
                                      .select("rect")
                                      .attr("fill",defaultColor);
                              }
                          })

  var bWidth= 160; //button width
  var bHeight= 50; //button height
  var bSpace= 10; //space between buttons
  var x0= 20; //x offset
  var y0= 10; //y offset

  //adding a rect to each toggle button group
  //rx and ry give the rect rounded corner
  buttonGroups.append("rect")
              .attr("class","buttonRect")
              .attr("width",bWidth)
              .attr("height",bHeight)
              .attr("x", x0)
              .attr("y",function(d,i) {return y0+(bHeight+bSpace)*i;})
              .attr("rx",5) //rx and ry give the buttons rounded corners
              .attr("ry",5)
              .attr("fill",defaultColor)


//adding text to each toggle button group, centered 
            //within the toggle button rect
            buttonGroups.append("text")
                        .attr("class","buttonText")
                        .attr("x",function(d,i) {
                            return x0 + bWidth/2;
                        })
                        .attr("y",function(d,i) {return y0+(bHeight+bSpace)*i + bHeight/2;})
                        .attr("text-anchor","middle")
                        .attr("dominant-baseline","central")
                        .attr("fill","white")
                        .text(function(d) {return d.charAt(0).toUpperCase() + d.slice(1).replace("C", " C").replace("A", " A");})

  function updateButtonColors(button, parent) {
      parent.selectAll("rect")
              .attr("fill",defaultColor)

      button.select("rect")
              .attr("fill",pressedColor)
  }






  // Create the defailed nutrition box
  var nutrientchart = d3.select("#overview")
        .append("div")
        .attr("class", "food-overview")
        .attr("id", "foodOverview")
        .classed("hidden", true);

  // Create GDA fulfillment box
  var gda = d3.select("#gda");
  gda.append("div")
        .attr("class", "gda-header")
        .text("Nutritional Overview");
  gda.append("div")
      .attr("class", "gda");
  gda.append("div")
      .attr("class", "gda-nutrient gda-nutrient-container")
      .append("span")
      .attr("class", "gda-percentage")
      .text("% Daily Value");
  d3.select("#selected")
        .append("div")
        .attr("class", "gda-header")
        .text("Selected Food");
  
  // Add Slider
  d3.select('#gda-slider').call(
    d3.slider().min(8).max(1).step(1).value(1).orientation("vertical").on("slide", 
      function(evt, value) {
          mouseclick(Math.round(value - 1));
      }
    )
  );
  
  // Create the selection menu, defailed info box, GDA fulfillment box
  for (var i = 0; i < nutrients.length; i++) {
      
    // Create GDA Fulfillment sections
    switch(nutrients[i]){
        case "vitaminA":
        case "magnesium":
          var tempcont = gda.append("div")
            .attr("class", "gda-nutrient-container vitamin-container")
            .attr("id", nutrients[i] + "-container")
          var nutrientcontainer = tempcont.append("div")
        break;
        case "vitaminC":
        case "iron":
          var nutrientcontainer = d3
            .select("#"+nutrients[i-1] + "-container").append("div")
        break;
        default:
          var nutrientcontainer = gda.append("div")
            .attr("class", "gda-nutrient-container")
        break;
    }
    
    nutrientcontainer.attr("id", "gda-" + nutrients[i])
    nutrientcontainer.append("span")
      .text(nutrients[i].charAt(0).toUpperCase() + nutrients[i].slice(1).replace("C", " C").replace("A", " A"))
      .attr("class", "gda-nutrient")
    nutrientcontainer.append("span")
      .attr("class", "gda-amount")
      .text("0" + units[i]);
    nutrientcontainer.append("span")
      .attr("class", "gda-percentage")
      .text("0%");
  }
  

  // Fired when a menu box is selected
  function mouseclick(value) {
    var targetid = nutrients[value]
    if (targetid && targetid != selected_nutrient) {
      
      // Set all backgrounds to default
      d3.selectAll(".gda-nutrient")
        .style("color", "#000");

      // Set selected box to highlighted color
      d3.select("#gda-" + targetid+" .gda-nutrient")
        .transition()
        .duration(100)
        .style("color", "#FF3030");
      
      // Update the selection variable with the new id
      selected_nutrient = targetid;
      
      // Remove all displayed nodes and regenerate graph
      d3.selectAll(".force-scale-node").remove();
      getScale(data, svg, selected_nutrient);
    }
  } 
}
