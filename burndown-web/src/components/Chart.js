import data from '../mockup-data.json'
import { VictoryChart, VictoryTheme, VictoryLine } from 'victory'

const Chart = () => {
  const parsedData = transformData(data.data)

  const fisrtData = parsedData[Object.keys(parsedData)[2]]

  // const values = Object.keys(fisrtData).map(date => ({ date: date, quantity: fisrtData[date] }))

  return (
    <VictoryChart
      theme={VictoryTheme.material}
    >
      <VictoryLine
        data={[
          { x: 1, y: 2 },
          { x: 2, y: 3 },
          { x: 3, y: 5 },
          { x: 4, y: 4 },
          { x: 5, y: 6 }
        ]}
      />

    </VictoryChart>
  );
};

function transformData(data) {
  const transformedData = {};

  data.forEach((day) => {
    const dateString = Object.keys(day)[0];
    const dayData = JSON.parse(day[dateString]);

    Object.keys(dayData)
      .forEach((status) => {
        if (!transformedData[status]) {
          transformedData[status] = {};
        }

        transformedData[status][dateString] = dayData[status]
      });
  });

  return transformedData;
}

export default Chart;
