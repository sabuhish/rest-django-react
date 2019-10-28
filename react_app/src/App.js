import React from 'react';
import {
  Card, CardImg, Col, CardText, CardBody,
  CardTitle, CardSubtitle, Button
} from 'reactstrap';

class App extends React.Component {


  state = {
    data: null
  }
  componentDidMount(){
    fetch("/api/cards")
      .then(response => response.json())
      .then(data => this.setState({data: data }));
  }

  render() {
    console.log(this.state.data);
    return (
     <div  className={"container mt-5"}>
       <div className="row">
         {this.state.data && this.state.data.map((item, index) => {
           return (<div className={"col-4"} key={index}>
                <Card>
                <CardImg top width="100%" src={item.img} alt="Card image cap" />
                <CardBody>
                  <CardTitle>{item.title}</CardTitle>
                  <CardSubtitle>{item.subtitle}</CardSubtitle>
                  <CardText>{item.description}</CardText>
                </CardBody>
              </Card>
           </div>)   
         })}
      
       </div>

     </div>
  );
}
}

export default App;
