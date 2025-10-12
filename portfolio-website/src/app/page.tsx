"use client";
import Image from "next/image";
import styles from "./page.module.css";
import {
  Button,
  Popover,
  Stack,
  TextareaAutosize,
  Typography,
} from "@mui/material";
import { useState } from "react";
import React from "react";

export default function Home() {
  const [anchorEl, setAnchorEl] = React.useState<HTMLButtonElement | null>(
    null
  );

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };
  const open = Boolean(anchorEl);

  return (
    <div className={styles.page}>
      <Button aria-describedby={"j"} variant="contained" onClick={handleClick}>
        Open Popover
      </Button>
      <Popover
        open={open}
        anchorEl={anchorEl}
        anchorOrigin={{
          vertical: "bottom",
          horizontal: "left",
        }}
        transformOrigin={{
          vertical: "top",
          horizontal: "left",
        }}
        onClose={handleClose}
      >
        <Stack
          height={500}
          width={300}
          sx={{
            justifyContent: "space-between",
          }}
        >
          <Typography>Know More About Vibhanshu</Typography>
          <Typography sx={{ flexGrow: 1 }}> Answers</Typography>
          <TextareaAutosize
            minRows={2}
            maxRows={4}
            style={{
              background: "white",
              color:"black",
              border: "solid black .5px",
              margin:"2px"
            }}
          />
        </Stack>
      </Popover>
    </div>
  );
}
