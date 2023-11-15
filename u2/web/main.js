let pastValue = 0;

async function get_data(){
    let data = await eel.get_data()();

    let plot = [{
          domain: { x: [0, 1], y: [0, 1] },
          value: data,
          title: { text: "Temperatura corporal" },
          type: "indicator",
          mode: "gauge+number+delta",
          delta: { reference: pastValue },
          gauge: { axis: { range: [null, 40] }},
        }
      ];
      
      pastValue = data;
      let layout = { 
        width: 600, 
        height: 400,
        paper_bgcolor: "transparent",
        font: {
          color: "white",
          family: "lato, sans-serif",
        }
      };
      Plotly.newPlot('myDiv', plot, layout);
}

setInterval(get_data, 20);