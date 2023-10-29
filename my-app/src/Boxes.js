import React from 'react';
import { Box, Flex } from '@chakra-ui/react';

function Boxes({ result1, result2, result3 }) {
  return (
    <Flex
      direction="row"
      w="100%" // Set the width to 100% to make it fill the page horizontally
      h="55vh" // Set the height of the container to 60vh for the entire viewport height
    //   bg="teal.1000"
    >
      <Box
        flex="1" // Let this box fill the available vertical space (bottom half)
        border="3px solid #ADD8E6" // Add a thin white border
        mx={2}
      >
        {result1}
      </Box>
      <Box
        flex="1" // Each box within the flex container will fill the horizontal space evenly
        border="3px solid #ADD8E6" // Add a thin white border
        mx={2}
      >
        {result2}
      </Box>
      <Box
        flex="1" // Each box within the flex container will fill the horizontal space evenly
        border="3px solid #ADD8E6" // Add a thin white border
        mx={2}
      >
        {result3}
      </Box>
    </Flex>
  );
}

export default Boxes;