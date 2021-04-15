function chart(frequency){
  const linechart = document.getElementsByTagName("canvas")[0].getContext("2d");

  var linechart_data = {
    type: "line",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
      datasets: [
        {
          label: "Earnings",
          fill: true,
          data: [
            "0",
            "10000",
            "5000",
            "15000",
            "10000",
            "20000",
            "15000",
            "25000",
          ],
          backgroundColor: "rgba(78, 115, 223, 0.05)",
          borderColor: "rgba(78, 115, 223, 1)",
        },
      ],
    },
    options: {
      maintainAspectRatio: false,
      legend: { display: false },
      title: {},
      scales: {
        xAxes: [
          {
            gridLines: {
              color: "rgb(234, 236, 244)",
              zeroLineColor: "rgb(234, 236, 244)",
              drawBorder: false,
              drawTicks: false,
              borderDash: ["2"],
              zeroLineBorderDash: ["2"],
              drawOnChartArea: false,
            },
            ticks: { fontColor: "#858796", padding: 20 },
          },
        ],
        yAxes: [
          {
            gridLines: {
              color: "rgb(234, 236, 244)",
              zeroLineColor: "rgb(234, 236, 244)",
              drawBorder: false,
              drawTicks: false,
              borderDash: ["2"],
              zeroLineBorderDash: ["2"],
            },
            ticks: { fontColor: "#858796", padding: 20 },
          },
        ],
      },
    },
  };


  var weekly_data;

  fetch(`/get_order_data/${frequency}`)
  .then(response => response.json())
  .then(data=> weekly_data = data)
  .then(()=>linechart_data["data"]["labels"] = Object.keys(weekly_data).slice(0,7))
  .then(()=> linechart_data["data"]["datasets"][0]["data"] = Object.keys(weekly_data).slice(0,7).map(function (key) {
    return JSON.stringify(weekly_data[key]);
  }))
  .then(()=>console.log(linechart_data))
  .then(()=>{mychart = new Chart(linechart,linechart_data)})
}
