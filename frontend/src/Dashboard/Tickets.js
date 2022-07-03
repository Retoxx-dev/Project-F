import React, { useState, useEffect } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from './Title';

function Dashboard(){

  const [tickets, ticketsData] = useState([])
  useEffect(() => {
    getTickets()
  }, [])

  const getTickets = () => {
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/tickets/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    }
    }).then((response) => response.json())
      .then((response) => {
        console.log(response);
        ticketsData(response);
    })
  }

  const [agents, agentsData] = useState([])
  useEffect(() => {
    getAgents()
  }, [])

  const getAgents = () => {
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/agents/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    }
    }).then((response) => response.json())
      .then((response) => {
        console.log(response);
        agentsData(response);
    })
  }

  const [customers, customersData] = useState([])
  useEffect(() => {
    getCustomers()
  }, [])

  const getCustomers = () => {
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/customers/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    }
    }).then((response) => response.json())
      .then((response) => {
        console.log(response);
        customersData(response);
    })
  }

  const [ticketTypes, ticketTypesData] = useState([])
  useEffect(() => {
    getTicketTypes()
  }, [])

  const getTicketTypes = () => {
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/tickettypes/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    }
    }).then((response) => response.json())
      .then((response) => {
        console.log(response);
        ticketTypesData(response);
    })
  }

  const [levels, levelsData] = useState([])
  useEffect(() => {
    getLevels()
  }, [])

  const getLevels = () => {
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/levels/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    }
    }).then((response) => response.json())
      .then((response) => {
        console.log(response);
        levelsData(response);
    })
  }

  const [statuses, statusesData] = useState([])
  useEffect(() => {
    getStatuses()
  }, [])

  const getStatuses = () => {
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/statuses/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    }
    }).then((response) => response.json())
      .then((response) => {
        console.log(response);
        statusesData(response);
    })
  }

  return (
    <React.Fragment>
      <Title>Tickets</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Ticket ID</TableCell>
            <TableCell>Customer</TableCell>
            <TableCell>Type</TableCell>
            <TableCell>Summary</TableCell>
            <TableCell>Description</TableCell>
            <TableCell>Status</TableCell>
            <TableCell>Level</TableCell>
            <TableCell>Assigned to</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {tickets.map((item, i) => (
            <TableRow key={i}>
            <TableCell>{item.id}</TableCell>
            <TableCell>{item.customer_username}</TableCell>
            <TableCell>{item.ticket_type_name}</TableCell>
            <TableCell>{item.summary}</TableCell>
            <TableCell>{item.description}</TableCell>
            <TableCell>{item.status_name}</TableCell>
            <TableCell>{item.level_name}</TableCell>
            <TableCell>{item.agent_username}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <Title>Agents</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Username</TableCell>
            <TableCell>Email</TableCell>
            <TableCell>Firstname</TableCell>
            <TableCell>Lastname</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {agents.map((item, i) => (
            <TableRow key={i}>
            <TableCell>{item.id}</TableCell>
            <TableCell>{item.username}</TableCell>
            <TableCell>{item.email}</TableCell>
            <TableCell>{item.firstname}</TableCell>
            <TableCell>{item.lastname}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <Title>Customers</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Username</TableCell>
            <TableCell>Email</TableCell>
            <TableCell>Firstname</TableCell>
            <TableCell>Lastname</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {customers.map((item, i) => (
            <TableRow key={i}>
            <TableCell>{item.id}</TableCell>
            <TableCell>{item.username}</TableCell>
            <TableCell>{item.email}</TableCell>
            <TableCell>{item.firstname}</TableCell>
            <TableCell>{item.lastname}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <Title>Statuses</Title>
      <Table size="large">
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Name</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {statuses.map((item, i) => (
            <TableRow key={i}>
            <TableCell>{item.id}</TableCell>
            <TableCell>{item.status_name}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <Title>Levels</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Name</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {levels.map((item, i) => (
            <TableRow key={i}>
            <TableCell>{item.id}</TableCell>
            <TableCell>{item.level_name}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <Title>Ticket Types</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Name</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {ticketTypes.map((item, i) => (
            <TableRow key={i}>
            <TableCell>{item.id}</TableCell>
            <TableCell>{item.ticket_type_name}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </React.Fragment>
  );
}

export default Dashboard;