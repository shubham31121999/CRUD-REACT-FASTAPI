import React, {useState,useEffect} from 'react';
import {Box,Button,Flex,Input,InputGroup,Modal,ModalBody,ModalCloseButton,ModalContent,ModalHeader,ModalFooter,ModalOverlay,Stack,Text,useDisclosure} from "@chakra-ui/react";

const TodoContext = React.createContext({
    todos :[],fetchTodos: ()=>{}
})


//Creating funtion component Todos
export default function Todos() {
    const[todos,setTodos] = useState([])
    const fetchTodos = async() => {
        const response = await fetch("http://127.0.0.1:8000/todo")
        const todos = await response.json()
        setTodos(todos.data)
    }

    //React hook to fetch the data
useEffect(() =>{
    fetchTodos()
},[])


return(
    <TodoContext.Provider value={{todos,fetchTodos}}>
        <Stack spacing={5}>
        {todos.map((todo)=>(
            <b>{todo.item}</b>
        ))}
        </Stack>
    </TodoContext.Provider>
)
}
