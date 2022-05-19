import * as React from "react";

export interface HelloProps {
    name: String,
}

const Hello: React.FunctionComponent<HelloProps> = (props: HelloProps) => {
    return (<div>Hello {props.name} </div>);
}

export default Hello;