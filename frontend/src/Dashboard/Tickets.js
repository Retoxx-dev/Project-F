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

  const [summary, setSummaryToAdd] = useState();
  const [description, setDescriptionToAdd] = useState();
  const [customer_id, setCustomerIDToAdd] = useState();
  const [status_id, setStatusIDToAdd] = useState();
  const [level_id, setLevelIDToAdd] = useState();
  const [agent_id, setAgentIDToAdd] = useState();
  const [ticket_type_id, setTicketTypeIDToAdd] = useState();
  const [date_occured, setDateOccuredToAdd] = useState();
  

  const postTickets = (ticket) => {
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/tickets/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    },
    body: JSON.stringify(ticket)
    })
  }

  function handleTicketCreation(){
    const response = postTickets({
      summary,
      description,
      customer_id,
      status_id,
      level_id,
      agent_id,
      ticket_type_id,
      date_occured
    })
  }

  function handleTicketDelete(ticket_id){
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/tickets/' + ticket_id, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    }
    }).then(window.location.href = "/")
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

  const [username, AgentsetUsernameToAdd] = useState();
  const [email, AgentsetEmailToAdd] = useState();
  const [firstname, AgentsetFirstnameToAdd] = useState();
  const [lastname, AgentsetLastnameToAdd] = useState();
  const [password, AgentsetPasswordToAdd] = useState();

  const postAgents = (agent) => {
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/agents/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    },
    body: JSON.stringify(agent)
    })
  }

  function handleAgentCreation(){
    const response = postAgents({
      username,
      email,
      firstname,
      lastname,
      password
    })
  }

  function handleAgentDelete(agent_id){
    const token = localStorage.getItem("access_token");
    fetch('http://localhost/api/agents/' + agent_id, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    }
    }).then(window.location.href = "/")
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
      <div className="d-flex flex-row">
        <button type="button" className="me-3 btn btn-primary ml-auto d-block mb-2" data-bs-toggle="modal" data-bs-target="#addModalForm">
          Add Ticket +
        </button>
      </div>      
      <table className="table table-bordered border-primary table-responsive">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Customer</th>
            <th scope="col">Summary</th>
            <th scope="col">Description</th>
            <th scope="col">Status</th>
            <th scope="col">Level</th>
            <th scope="col">Assigned to</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
        {tickets.map((ticket, i) => (
          <tr>
            <td>{ticket.id}</td>
            <td>{ticket.customer_username}</td>
            <td>{ticket.summary}</td>
            <td>{ticket.description}</td>
            <td>{ticket.status_name}</td>
            <td>{ticket.level_name}</td>
            <td>{ticket.agent_username}</td>
            <td>
              <button type="button" className="btn btn-danger" aria-label="Delete" onClick={()=>handleTicketDelete(ticket.id)}>Delete</button>
            </td>
          </tr>
        ))}
        </tbody>
      </table>
      {/*Add Modal */}
      <div className="modal fade" id="addModalForm" tabIndex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="exampleModalLabel">Add New Ticket</h5>
              <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div className="modal-body">
              <form onSubmit={handleTicketCreation}>
                <div className="mb-3">
                  <label className="form-label">Summary</label>
                  <input
                    type="text"
                    className="form-control"
                    name="Summary"
                    placeholder="Summary"
                    required
                    onChange={e => setSummaryToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Description</label>
                  <textarea
                    rows="4"
                    cols="50"
                    className="form-control"
                    name="Description"
                    placeholder="Description"
                    required
                    onChange={e => setDescriptionToAdd(e.target.value)}
                  ></textarea>
                </div>
                <div className="mb-3">
                  <label className="form-label">Customer ID</label>
                  <input
                    type="text"
                    className="form-control"
                    name="Description"
                    placeholder="Description"
                    required
                    onChange={e => setCustomerIDToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Status ID</label>
                  <input
                    type="text"
                    className="form-control"
                    name="StatusID"
                    placeholder="StatusID"
                    required
                    onChange={e => setStatusIDToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Level ID</label>
                  <input
                    type="text"
                    className="form-control"
                    name="LevelID"
                    placeholder="LevelID"
                    required
                    onChange={e => setLevelIDToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Agent ID</label>
                  <input
                    type="text"
                    className="form-control"
                    name="AgentID"
                    placeholder="AgentID"
                    required
                    onChange={e => setAgentIDToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Ticket Type ID</label>
                  <input
                    type="text"
                    className="form-control"
                    name="TicketTypeID"
                    placeholder="TicketTypeID"
                    required
                    onChange={e => setTicketTypeIDToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Date Occured</label>
                  <input
                    type="date"
                    className="form-control"
                    name="DateOccured"
                    placeholder="DateOccured"
                    required
                    onChange={e => setDateOccuredToAdd(e.target.value)}
                  />
                </div>
                <div className="modal-footer d-block">
                  <button type="submit" data-bs-dismiss="modal" className="btn btn-warning float-end">Submit</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      
      <Title>Agents</Title>
      <div className="d-flex flex-row">
        <button type="button" className="me-3 btn btn-primary ml-auto d-block mb-2" data-bs-toggle="modal" data-bs-target="#addAgentModalCreateForm">
          Add Agent +
        </button>
      </div>      
      <table className="table table-bordered border-primary table-responsive">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Username</th>
            <th scope="col">Email</th>
            <th scope="col">Firstname</th>
            <th scope="col">Lastname</th>
          </tr>
        </thead>
        <tbody>
        {agents.map((agent, i) => (
          <tr>
            <td>{agent.id}</td>
            <td>{agent.username}</td>
            <td>{agent.email}</td>
            <td>{agent.firstname}</td>
            <td>{agent.lastname}</td>
            <td>
              <button type="button" className="btn btn-danger" aria-label="Delete" onClick={()=>handleAgentDelete(agent.id)}>Delete</button>
            </td>
          </tr>
        ))}
        </tbody>
      </table>
      {/*Add Modal */}
      <div className="modal fade" id="addAgentModalCreateForm" tabIndex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h5 className="modal-title" id="exampleModalLabel">Add New Agent</h5>
              <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div className="modal-body">
              <form onSubmit={handleAgentCreation}>
                <div className="mb-3">
                  <label className="form-label">Username</label>
                  <input
                    type="text"
                    className="form-control"
                    name="Username"
                    placeholder="Username"
                    required
                    onChange={e => AgentsetUsernameToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Email</label>
                  <input
                    type="text"
                    className="form-control"
                    name="Email"
                    placeholder="Email"
                    required
                    onChange={e => AgentsetEmailToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">First Name</label>
                  <input
                    type="text"
                    className="form-control"
                    name="First Name"
                    placeholder="First Name"
                    required
                    onChange={e => AgentsetFirstnameToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Last Name</label>
                  <input
                    type="text"
                    className="form-control"
                    name="Last Name"
                    placeholder="Last Name"
                    required
                    onChange={e => AgentsetLastnameToAdd(e.target.value)}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Password</label>
                  <input
                    type="password"
                    className="form-control"
                    name="Password"
                    required
                    onChange={e => AgentsetPasswordToAdd(e.target.value)}
                  />
                </div>
                <div className="modal-footer d-block">
                  <button type="submit" data-bs-dismiss="modal" className="btn btn-warning float-end">Submit</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>




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