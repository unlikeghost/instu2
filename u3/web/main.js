async function get_data(){
  let data = await eel.get_data()();

  let len = data.length;

  let trace1 = {
    x: Array.from(Array(len).keys()),
    y: data,
    type: 'scatter',
    line: {color: "rgb(0,0,0)",
           width: 3,
           dtick: 0.25,
          },
  };

  let layout = {
    plot_bgcolor: "rgb(230,188,197)", 
    xaxis: {
      gridcolor: "rgb(208,160,172)",
      autotick: false,
      ticks: 'outside',
      dtick: 10,
      ticklen: 8,
      title: {
        text: 'Time (ms)',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      },

    }, 
    yaxis: {
      gridcolor: "rgb(208,160,172)",
      autotick: true,
      dtick: 100,
      ticklen: 8,
      title: {
        text: 'Voltage (mV)',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        },
      },

    }

  }
  let plots = [trace1];

  Plotly.newPlot('myDiv', plots, layout);

}

setInterval(get_data, 5);