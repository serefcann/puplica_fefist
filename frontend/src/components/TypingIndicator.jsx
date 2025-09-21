import React from 'react'

const TypingIndicator = () => {
  return (
    <div className="flex justify-start">
      <div className="flex flex-col max-w-4xl">
        <div className="bot-message message-bubble">
          <div className="flex items-center space-x-2 text-sm text-white">
            <span className="italic">Model düşünüyor</span>
            <div className="flex space-x-1">
              <div className="w-2 h-2 bg-white bg-opacity-70 rounded-full animate-pulse"></div>
              <div className="w-2 h-2 bg-white bg-opacity-70 rounded-full animate-pulse" style={{ animationDelay: '0.2s' }}></div>
              <div className="w-2 h-2 bg-white bg-opacity-70 rounded-full animate-pulse" style={{ animationDelay: '0.4s' }}></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default TypingIndicator


