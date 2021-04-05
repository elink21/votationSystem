var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Cientific party', 'Workers party', 'Democrat party'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3],
            backgroundColor: [
                '#18A558',
                '#A3EBB1',
                '#21B6A8'
            ],
            borderWidth: 1
        }]
    },
    options: {
        animation: {
            duration: 500
        },
        plugins: {
            title: {
                display: true,
                text: 'Realtime election results'
            }
        }
    }
});



let requestUpdate = () => {
    $.ajax(
        {
            url: 'requestUpdate',
            success: function (newData) {
                console.log("Requested");
                updateChart(newData);
            }

        }
    );

}

let realTime = setInterval(requestUpdate, 1000);



const updateChart = (newVotes) => {
    let newData = [newVotes.scientificVotes, newVotes.workersVotes, newVotes.democratVotes];
    console.table(newData);

    myChart.data.datasets.pop();

    const newDataset = {
        label: '# Of votes ',
        data: newData,
        backgroundColor: [
            '#18A558',
            '#A3EBB1',
            '#21B6A8'
        ],
        borderWidth: 1
    };

    myChart.data.datasets.push(newDataset);


    myChart.update();
}