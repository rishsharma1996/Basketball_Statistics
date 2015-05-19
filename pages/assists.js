$(function () {
    $('#container').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Count of Assists Throughout 1999-2007.'
        },
        subtitle: {
            text: 'Source: http://www.basketball-reference.com/'
        },
        xAxis: {
            categories: [
                '1999-00',
                '2000-01',
                '2001-02',
                '2002-03',
                '2003-04',
                '2004-05',
                '2005-06',
                '2006-07'
                
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Count'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: '0-1',
            data: [162, 165, 167, 170, 167, 175, 190, 193]

        }, {
            name: '1-2',
            data: [106, 98, 111, 103, 85, 103, 93, 108]

        }, {
            name: '2-3',
            data: [63, 47, 55, 52, 53, 54, 53, 46]

        }, {
            name: '3-4',
            data: [34, 37, 30, 30, 21, 25, 25, 32]

        },
            {
            name: '4-5',
            data: [20, 21, 12, 20, 19, 17, 20, 21]

        },
                 
             {
            name: '5-6',
            data: [9, 7, 18, 13, 17, 13, 7, 14]

        },
             {
            name: '6-7',
            data:[3, 7, 6, 6, 8, 11, 11, 7]

        },

             {
            name: '7-8',
            data: [5, 6, 3, 4, 2, 3, 2, 3]

        },


             {
            name: '8-9',
            data:  [6, 5, 6, 3, 1, 3, 5, 2]

        },

             {
            name: '9-10',
            data: [2, 1, 1, 'null', 1, 'null', 'null', 2]

        }                ]
    });
});