import { Bar } from "react-chartjs-2";

/** eslint-disable react/prop-types */

export default function StatsChart({ stats }: any) {
    const data = {
        labels: stats.map((s: any) => s.operation),
        datasets: [
            {
                label: "Average Time (ms)",
                data: stats.map((s: any) => s.avg_time),
                backgroundColor: "rgba(75, 192, 192, 0.6)",
            },
        ],
    };

    return (
        <div className="stats-chart">
            <Bar data={data} />
        </div>
    );
}