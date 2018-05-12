import * as React from "react";
import { Table } from "react-bootstrap";
import Axios from "axios";

interface Item {
    id: number;
    name: string;
    status: string;
}
export default class PatioTable extends React.Component<{}, { data: Item[]}> {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        };
    }

    getEquipments() {
        var that = this;
        Axios.get<Item[]>('/api/equipments').then(function (response) {
            that.setState({
                data: response.data
            });
        });
    }

    componentWillMount() {

        this.getEquipments();

    }

    render() {
        return (
            <div>
                <Table striped bordered condensed hover>
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Name</th>
                        <th>Status</th>
                    </tr>
                    </thead>
                    <tbody>
                        {
                            this.state.data.map(item =>
                                <tr key={item.id}>
                                    <td>{item.id}</td>
                                    <td>{item.name}</td>
                                    <td>{item.status}</td>
                                </tr>
                            )
                        }
                    </tbody>
                </Table>
            </div>
        )
    }
}
