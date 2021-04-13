function func(){
    var ctx = document.getElementById('myChart').getContext('2d');

var dict = {
    'SUN': Math.floor(Math.random() * 50)+50,
    'MON': Math.floor(Math.random() * 50)+50,
    'TUE': Math.floor(Math.random() * 50)+50,
    'WED': Math.floor(Math.random() * 50)+50,
    'THU': Math.floor(Math.random() * 50)+50,
    'FRI': Math.floor(Math.random() * 50)+50,
    'SAT': Math.floor(Math.random() * 50)+50
  };


var mychart = new Chart(ctx , {
        
        type : "line",
        data: {
            labels : Object.keys(dict),
            datasets: [
                {
                data :Object.keys(dict).map(function (key) { return dict[key]; }),
                label : "Sales",
                fill: false,
                backgroundColor : '#0062ff',
                pointBackgroundColor: '#0062ff',
                pointHoverBackgroundColor: '#0062ff',
                borderColor: '#0062ff',
                pointBorderColor: '#0062ff',
                pointHoverBorderColor: '#0062ff',
                //backgroundColor : ["blue" , "red" , "black" ,"green","pink" ,"orange" , "yellow"],
                borderWidth : 1,

        },
    ],
},



options : {
    responsive: true,
    maintainAspectRatio: true,
    layout:{
        padding: {
            left: 15,
            top:  50,
        }
    },
    title: {
        display:true,
        text: "SALES PREDICTION",
        fontSize : 25,
    },
    animation:{
        duration:5000,
    }
}





})
}