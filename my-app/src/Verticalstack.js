import { Box, Heading, Stack } from '@chakra-ui/react';
import SearchBar from './SearchBar';
import Boxes from './Boxes';
import React, { useState } from 'react';

export default function Verticalstack() {
const [searchQuery, setSearchQuery] = useState(''); // State to store the search query
const [result1, setResult1] = useState([]); // state to store the results from the search
const [result2, setResult2] = useState([]);
const [result3, setResult3] = useState([]);

const fetchData = async () => {
  try {
      const response = await fetch(`http://0.0.0.0:8080/api/v1/query?question=${encodeURIComponent(searchQuery)}`);
      if (response.ok) {
          const jsonData = await response.json();
          console.log(jsonData);
          setResult1(jsonData.message['ret_list'][0]);
          setResult2(jsonData.message['ret_list'][1]);
          setResult3(jsonData.message['ret_list'][2]);
          // setData(jsonData);
      } else {
          console.error('Failed to fetch data', response.statusText);
      }
  } catch (error) {
      console.error('Error fetching data:', error);
  }
};
const handleSearch = () => {
    // You can perform any actions with the searchQuery here, like sending it to a server or updating state in a parent component.
    // sending this to backend
    // console.log("Search query:", searchQuery);
    fetchData();
  };

  return (
    <Stack direction={'column'} spacing={5}>
      <Box p={4}>
        <Heading as="h1" size="xl">
          SecondSearch 
        </Heading>
        <Heading as="h2" size="sm" marginTop={8}>
          Pick your class, then type your query in the box below!
        </Heading>
      </Box>
      <SearchBar searchQuery={searchQuery} setSearchQuery={setSearchQuery} handleSearch={handleSearch}/>
      <Boxes result1={result1} result2={result2} result3={result3} />
    </Stack>
  );
}
