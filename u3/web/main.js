async function get_data() {
  let data = await eel.get_data()();

  let len = data.length;

  let trace1 = {
    bgcolor: "transparent",
    x: Array.from(Array(len).keys()),
    y: data,
    type: 'scatter',
    line: {
      color: "rgb(199, 248, 228)",
      width: 3,
      dtick: 0.25,
    },

  };

  let layout = {
    plot_bgcolor: "transparent",
    paper_bgcolor: "transparent",
    font: {
      color: "white",
      family: "lato, sans-serif",
    },
    xaxis: {
      gridcolor: "rgb(0,155,158)",
      autotick: false,
      ticks: 'outside',
      dtick: 10,
      ticklen: 8, 
      title: {
        text: 'Time (ms)',
        font: {
          family: "lato, sans-serif",
          size: 18,
          color: '#fff'
        }
      },

    },
    yaxis: {
      gridcolor: "rgb(0,155,158)",
      autotick: true,
      dtick: 100,
      ticklen: 8,
      title: {
        text: 'Voltage (mV)',
        font: {
          family: "lato, sans-serif",
          size: 18,
          color: '#fff'
        },
      },

    }

  }
  let plots = [trace1];

  Plotly.newPlot('myDiv', plots, layout);

}

setInterval(get_data, 5);