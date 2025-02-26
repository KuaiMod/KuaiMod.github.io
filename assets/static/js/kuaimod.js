var dom = document.getElementById('container-object');
var myChart = echarts.init(dom, null, {
  renderer: 'svg',
  useDirtyRect: false
});
var app = {};
var option;


var data = [
{
    name: 'KuaiMod',
    itemStyle: {
    color: 'white'
    },
    children: [
    {
        name: '',
        itemStyle: {
        color: '#EE7C30'
        },
children: [
{
    name: 'Legal Issues',
    itemStyle: {
    color: '#C76DA2',
    },
    children: [
    {
        name: 'Illegal \nActivities (50)',
        value: 1,
        itemStyle: {
        color: '#f5addc'// '#CC7EB1'
        }
    },
    {
        name: 'Political Issues (56)',
        value: 1,
        itemStyle: {
        color: '#CC7EB1' //'#AA4C8F'
        }
    },
    {
        name: 'Hate Speech (52)',
        value: 1,
        itemStyle: {
        color: '#AA4C8F'//'#824880'
        }
    },
    {
        name: 'Prohibited\nItems Sales (1)',
        value: 1,
        itemStyle: {
        color: '#824880'
        }
    },
    {
        name: 'Historical\nRevisionism (11)',
        value: 1,
        itemStyle: {
        color: '#8f579a'
        }
    }
    ]
},
{
    name: 'Content Ethics',
    itemStyle: {
    color: '#5C9291'
    },
    children: [
    {
        name: 'Vulgar Content (114)',
        value: 1,
        itemStyle: {
        color: '#80989B'
        }
    },
    {
        name: 'Misinformation (54)',
        value: 1,
        itemStyle: {
        color: '#6C848D'
        }
    },
    {
        name: 'Harm to Minors (2)',
        value: 1,
        itemStyle: {
        color: '#4C6473'
        }
    },
    {
        name: 'Inappropriate Minor\nBehavior (10)',
        value: 1,
        itemStyle: {
        color: '#165E85'
        }
    }
    ]
},
{
    name: 'Commercial Behavior',
    itemStyle: {
    color: '#C89B40'
    },
    children: [
    {
        name: 'Exaggerated \nClaims (9)',
        value: 1,
        itemStyle: {
        color: '#D0AF4C'
        }
    },
    {
        name: 'Private\nTransactions (34)',
        value: 1,
        itemStyle: {
        color: '#C89932'
        }
    },
    {
        name: 'False Promises (4)',
        value: 1,
        itemStyle: {
        color: '#94846A'
        }
    },
    {
        name: 'Hype Marketing (8)',
        value: 1,
        itemStyle: {
        color: '#8F8667'
        }
    }
    ]
},
{
    name: 'Intellectual Property',
    itemStyle: {
    color: '#D76364'
    },
    children: [
    {
        name: 'Missing \nAI Marking (7)',
        value: 1.5,
        itemStyle: {
        color: '#A86965'
        }
    },
    {
        name: 'Plagiarism (10)',
        value: 1.5,
        itemStyle: {
        color: '#C97586'
        }
    }
    ]
}
]

    }
    ]
}
];
  
option = {
textStyle: {
    fontStyle: 'normal',
    fontFamily: "serif",
    fontSize: 17,
    width: 5,
    overflow: 'breakAll'
},
series: {
    type: 'sunburst',
    data: data,
    radius: ['15%', '80%'],
    sort: undefined,
    emphasis: {
    focus: 'ancestor'
    },
    levels: [
    {
        // Root Level
    },
    {
        r0: '0%',
        r: '1%',
        itemStyle: {
        // borderWidth: 2,
        // borderRadius: 10,
        opacity: 0.75,
            shadowColor: 'grey',
        // shadowBlur: 20
        },
        label: {
        rotate: 'tangential',
        align: 'center',
        color: 'brown',
        fontStyle: 'normal',
            fontFamily: 'Microsoft YaHei',
        fontSize: 25,
        fontWeight: "bold"
        }
    },
    {
        r0: '18%',
        r: '20%',
        itemStyle: {
        borderWidth: 5,
            borderRadius: 20,
            opacity: 0.75,
            shadowColor: 'grey',
        // shadowBlur: 20
        },
        label: {
        rotate: 'tangential',
        align: 'center',
        color: 'white',
        fontSize: 24,
        fontWeight: "bold"
        }
    },
    {
    r0: '20%',
    r: '45%',
    label: {
        align: 'center',
        fontSize: 20,
        fontWeight: "bold",
        color: 'black',
        rotate: 'tangential',
        overflow: 'break', // Allow breaking text
        formatter: function (params) {
        // Automatically insert line breaks based on text length
        const words = params.name.split(' ');
        let result = '';
        let line = '';
        for (let i = 0; i < words.length; i++) {
            if ((line + words[i]).length > 10) { // Adjust the length as needed
            result += line + '\n';
            line = '';
            }
            line += words[i] + ' ';
        }
        result += line; // Add the last line
        return result;
        },
    },
    itemStyle: {
        rotate: 'tangential',
        opacity: 0.8,
        borderWidth: 4,
        borderRadius: 20,
        shadowColor: 'grey',
        // shadowBlur: 40
    },
    },
    {
        r0: '45%',
        r: '100%',
        label: {
        // position: 'outside',
        padding: 0,
        fontSize: 17,
        color: '#4F4F4F',
        silent: true,
        fontWeight: "bold"
        },
        itemStyle: {
        borderWidth: 5,
        opacity: 0.7,
        borderRadius: 10,
        shadowColor: 'grey',
        
        // shadowBlur: 10
        }
    }
    ]
}
};
if (option && typeof option === 'object') {
  myChart.setOption(option);
}

window.addEventListener('resize', myChart.resize);
