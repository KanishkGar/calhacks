import { Box, Heading, Stack } from '@chakra-ui/react';
import SearchBar from './SearchBar';
import Boxes from './Boxes';
import React, { useState } from 'react';

export default function Verticalstack() {
const [searchQuery, setSearchQuery] = useState(''); // State to store the search query
const [result1] = useState(''); // state to store the results from the search
const [result2] = useState('');
const [result3] = useState('');

const handleSearch = () => {
    // You can perform any actions with the searchQuery here, like sending it to a server or updating state in a parent component.
    // sending this to backend
    // console.log("Search query:", searchQuery);

  };

  return (
    <Stack direction={'column'} spacing={5}>
      <Box p={4}>
        <Heading as="h1" size="xl">
          Hellooooo
        </Heading>
        <Heading as="h2" size="sm" marginTop={2}>
          insert brief description of what this project is lol
        </Heading>
      </Box>
      <SearchBar searchQuery={searchQuery} setSearchQuery={setSearchQuery} handleSearch={handleSearch}/>
      <Boxes result1={result1} result2={result2} result3={result3} />
    </Stack>
  );
}
