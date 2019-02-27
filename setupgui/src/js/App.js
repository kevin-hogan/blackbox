import React from 'react';
import CytoscapeComponent from 'react-cytoscapejs';

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
        node_count: 0
    };

    this.addNode = this.addNode.bind(this);
  }

  addNode() {
    this.setState(state => ({
      node_count: state.node_count + 1
    }));
  }

  render(){
    const nexus = [
      { data: { id: 'nexus', label: 'Switch' }, position: { x: 100, y: 100 } }
    ];

    const nodes = [...Array(this.state.node_count).keys()].map(i => {
      return [
        { data: { id: i, label: 'Node ' + i }, position: { x: 200, y: 50 + i*(100/this.state.node_count) } },
        { data: { source: 'nexus', target: i, label: '' } }
      ];
    }).flat();

    return <div>
            <CytoscapeComponent elements={nexus.concat(nodes)} style={ { width: '600px', height: '600px' } } />
            <button onClick={this.addNode}>Add Node (Total: {this.state.node_count})</button>
        </div>;
  }
}

export default App