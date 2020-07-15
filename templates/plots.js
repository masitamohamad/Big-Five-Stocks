var arr = ["amazon.csv", "facebook.csv","google.csv","microsoft.csv","apple.csv"]
    Plotly.d3.csv(arr[0], function (error, rows) {
      function unpack(rows, key) {
        return rows.map(function (row) {
          return row[key];
        });
      }
      var trace = {
        // type: "candlestick",
        // mode: "lines",
        name: String(arr[0]),
        x: unpack(rows, 'date'),
        close: unpack(rows, 'close'),
        decreasing: {
          line: {
            color: '#7F7F7F'
          }
        },
        high: unpack(rows, 'high'),
        increasing: {
          line: {
            color: '#3A858C'
          }
        },
        low: unpack(rows, 'low'),
        open: unpack(rows, 'open'),
        type: 'candlestick',
        xaxis: 'x',
        yaxis: 'y'
      };
      var layout = {
        dragmode: 'zoom',
        font: {
          family: 'Segoe UI',
          size: 14
        },
        margin: {
          r: 10,
          t: 25,
          b: 40,
          l: 60
        },
        showlegend: true,
        //     xaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: ['2017-01-03 12:00', '2017-02-15 12:00'], 
        //       rangeslider: {range: ['2017-01-03 12:00', '2017-02-15 12:00']}, 
        //       title: 'Date', 
        //       type: 'date'
        //     }, 
        //     yaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: [114.609999778, 137.410004222], 
        //       type: 'linear'
        //     }
      };
      Plotly.newPlot('plot-1', [trace],layout);
    })
    Plotly.d3.csv(arr[1], function (error, rows) {
      function unpack(rows, key) {
        return rows.map(function (row) {
          return row[key];
        });
      }
      var trace = {
        // type: "candlestick",
        // mode: "lines",
        name: String(arr[1]),
        x: unpack(rows, 'date'),
        close: unpack(rows, 'close'),
        decreasing: {
          line: {
            color: '#7F7F7F'
          }
        },
        high: unpack(rows, 'high'),
        increasing: {
          line: {
            color: '#3A858C'
          }
        },
        low: unpack(rows, 'low'),
        open: unpack(rows, 'open'),
        type: 'candlestick',
        xaxis: 'x',
        yaxis: 'y'
      };
      var layout = {
        dragmode: 'zoom',
        font: {
          family: 'Segoe UI',
          size: 14
        },
        margin: {
          r: 10,
          t: 25,
          b: 40,
          l: 60
        },
        showlegend: false,
        //     xaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: ['2017-01-03 12:00', '2017-02-15 12:00'], 
        //       rangeslider: {range: ['2017-01-03 12:00', '2017-02-15 12:00']}, 
        //       title: 'Date', 
        //       type: 'date'
        //     }, 
        //     yaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: [114.609999778, 137.410004222], 
        //       type: 'linear'
        //     }
      };
      Plotly.newPlot('plot-2', [trace],layout);
    })
    Plotly.d3.csv(arr[2], function (error, rows) {
      function unpack(rows, key) {
        return rows.map(function (row) {
          return row[key];
        });
      }
      var trace = {
        // type: "candlestick",
        // mode: "lines",
        name: String(arr[2]),
        x: unpack(rows, 'date'),
        close: unpack(rows, 'close'),
        decreasing: {
          line: {
            color: '#7F7F7F'
          }
        },
        high: unpack(rows, 'high'),
        increasing: {
          line: {
            color: '#3A858C'
          }
        },
        low: unpack(rows, 'low'),
        open: unpack(rows, 'open'),
        type: 'candlestick',
        xaxis: 'x',
        yaxis: 'y'
      };
      var layout = {
        dragmode: 'zoom',
        font: {
          family: 'Segoe UI',
          size: 14
        },
        margin: {
          r: 10,
          t: 25,
          b: 40,
          l: 60
        },
        showlegend: true,
        //     xaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: ['2017-01-03 12:00', '2017-02-15 12:00'], 
        //       rangeslider: {range: ['2017-01-03 12:00', '2017-02-15 12:00']}, 
        //       title: 'Date', 
        //       type: 'date'
        //     }, 
        //     yaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: [114.609999778, 137.410004222], 
        //       type: 'linear'
        //     }
      };
      Plotly.newPlot('plot-3', [trace],layout);
    })
    Plotly.d3.csv(arr[3], function (error, rows) {
      function unpack(rows, key) {
        return rows.map(function (row) {
          return row[key];
        });
      }
      var trace = {
        // type: "candlestick",
        // mode: "lines",
        name: String(arr[3]),
        x: unpack(rows, 'date'),
        close: unpack(rows, 'close'),
        decreasing: {
          line: {
            color: '#7F7F7F'
          }
        },
        high: unpack(rows, 'high'),
        increasing: {
          line: {
            color: '#3A858C'
          }
        },
        low: unpack(rows, 'low'),
        open: unpack(rows, 'open'),
        type: 'candlestick',
        xaxis: 'x',
        yaxis: 'y'
      };
      var layout = {
        dragmode: 'zoom',
        font: {
          family: 'Segoe UI',
          size: 14
        },
        margin: {
          r: 10,
          t: 25,
          b: 40,
          l: 60
        },
        showlegend: true,
        //     xaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: ['2017-01-03 12:00', '2017-02-15 12:00'], 
        //       rangeslider: {range: ['2017-01-03 12:00', '2017-02-15 12:00']}, 
        //       title: 'Date', 
        //       type: 'date'
        //     }, 
        //     yaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: [114.609999778, 137.410004222], 
        //       type: 'linear'
        //     }
      };
      Plotly.newPlot('plot-4', [trace],layout);
    })
    Plotly.d3.csv(arr[4], function (error, rows) {
      function unpack(rows, key) {
        return rows.map(function (row) {
          return row[key];
        });
      }
      var trace = {
        // type: "candlestick",
        // mode: "lines",
        name: String(arr[4]),
        x: unpack(rows, 'date'),
        close: unpack(rows, 'close'),
        decreasing: {
          line: {
            color: '#7F7F7F'
          }
        },
        high: unpack(rows, 'high'),
        increasing: {
          line: {
            color: '#3A858C'
          }
        },
        low: unpack(rows, 'low'),
        open: unpack(rows, 'open'),
        type: 'candlestick',
        xaxis: 'x',
        yaxis: 'y'
      };
      var layout = {
        dragmode: 'zoom',
        font: {
          family: 'Segoe UI',
          size: 14
        },
        margin: {
          r: 10,
          t: 25,
          b: 40,
          l: 60
        },
        showlegend: true,
        //     xaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: ['2017-01-03 12:00', '2017-02-15 12:00'], 
        //       rangeslider: {range: ['2017-01-03 12:00', '2017-02-15 12:00']}, 
        //       title: 'Date', 
        //       type: 'date'
        //     }, 
        //     yaxis: {
        //       autorange: true, 
        //       domain: [0, 1], 
        //       range: [114.609999778, 137.410004222], 
        //       type: 'linear'
        //     }
      };
      Plotly.newPlot('plot-5', [trace],layout);
    })